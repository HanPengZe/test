#include "Chassis.h"
#include "M6020_Motor.h"
#include "DR16_Remote.h"
#include "M3508_Motor.h"


incrementalpid_t LFWheel_PID = LFWHEEL_PID_PARAM;
#undef LFWHEEL_PID_PARAM
incrementalpid_t RFWheel_PID = RFWHEEL_PID_PARAM;
#undef RFWHEEL_PID_PARAM
incrementalpid_t LBWheel_PID = LBWHEEL_PID_PARAM;
#undef LBWHEEL_PID_PARAM
incrementalpid_t RBWheel_PID = RBWHEEL_PID_PARAM;
#undef RBWHEEL_PID_PARAM
incrementalpid_t *Wheel_PID[] = {&LFWheel_PID, &RFWheel_PID, &LBWheel_PID, &RBWheel_PID};

positionpid_t FollowYawAttitude_pid = FollowYawAttitude_pidInit; //����Yaw�������̨pid
positionpid_t FollowYawSpeed_pid = FollowYawSpeed_pidInit; //����Yaw�������̨pid
Chassis_t Chassis;
int ComputeMinOffset(int target, int value) 
{
    int err = target - value;

    if (err > 4096)
    {
        err -= 8191;
    }
    else if (err < -4096)
    {
        err += 8191;
    }
    return err;
}
static CAN_TxHeaderTypeDef  chassis_tx_message;
static uint8_t              chassis_can_send_data[8];
void set_3508_current(int16_t motor1, int16_t motor2, int16_t motor3, int16_t motor4)
{
    uint32_t send_mail_box;
    chassis_tx_message.StdId = CAN_CHASSIS_ALL_ID;
    chassis_tx_message.IDE = CAN_ID_STD;
    chassis_tx_message.RTR = CAN_RTR_DATA;
    chassis_tx_message.DLC = 0x08;
    chassis_can_send_data[0] = motor1 >> 8;
    chassis_can_send_data[1] = motor1;
    chassis_can_send_data[2] = motor2 >> 8;
    chassis_can_send_data[3] = motor2;
    chassis_can_send_data[4] = motor3 >> 8;
    chassis_can_send_data[5] = motor3;
    chassis_can_send_data[6] = motor4 >> 8;
    chassis_can_send_data[7] = motor4;

    HAL_CAN_AddTxMessage(&hcan1, &chassis_tx_message, chassis_can_send_data, &send_mail_box);

}


void Chassis_Follow( int Yaw_Center)
{
	float Angle = ComputeMinOffset(Yaw_Center, M6020s_Yaw.realAngle);//6020���㴦��
	float angle = Angle / (float)M6020_mAngleRatio;                  //6020ʵ�ʽǶ�
//	if(angle<=15&&angle>=-15)
//	{
//		angle=0;
//	}
	Chassis.In_Put= FollowYawAttitude_pid.Position_PID(&FollowYawAttitude_pid,0.0f ,angle );//�⻷����̨�͵�����ԽǶ�Ŀ��Ϊ�㣬�Ƕȵ�λ�ÿ��ƣ��������Ϊ�ڻ�������
	Chassis.Out_Put= FollowYawSpeed_pid.Position_PID(&FollowYawSpeed_pid, FollowYawAttitude_pid.pwm,M6020s_Yaw.realSpeed);//�⻷�����ֵ��Ϊ�����ٶȣ���6020�ĵ�ǰ�ٶȱջ�
//	FollowYawSpeed_pid.Position_PID(&FollowYawSpeed_pid, FollowYawAttitude_pid.pwm,motor_chassis[4].speed_rpm);//�⻷�����ֵ��Ϊ�����ٶȣ���6020�ĵ�ǰ�ٶȱջ�
	
//	set_2006_current(-FollowYawSpeed_pid.pwm,-FollowYawSpeed_pid.pwm,-FollowYawSpeed_pid.pwm,-FollowYawSpeed_pid.pwm);
	
}
void MecanumCalculate(float Vx, float Vy, float VOmega, int16_t *Speed)
{
    float tempSpeed[4];
//    float MaxSpeed = 0.0f;
    float Param = 1.0f;

    //�����ٶȷֽ�
    tempSpeed[0] = (Vx -Vy + VOmega	)*1.7f	;
    tempSpeed[1] = (-Vx -Vy + VOmega	)*1.7f	;
    tempSpeed[2] = (-Vx + Vy + VOmega)* 1.7f	;
    tempSpeed[3] = (+Vx +Vy + VOmega)* 1.7f;
																					
//    //Ѱ������ٶ�
//    for (uint8_t i = 0; i < 4; i++)
//    {
//        if (abs_t(tempSpeed[i]) > MaxSpeed)
//        {
//            MaxSpeed = abs_t(tempSpeed[i]);
//        }
//    }

//    //�ٶȷ���
//    if (MaxSpeed > WheelMaxSpeed)
//    {
//        Param = (float)WheelMaxSpeed / MaxSpeed;
//    }

    Speed[0] = tempSpeed[0] * Param;
    Speed[1] = tempSpeed[1] * Param;
    Speed[2] = tempSpeed[2] * Param;
    Speed[3] = tempSpeed[3] * Param;
}

void Chassis_Move(int16_t *speed)
{
	 for (int i = 0; i < 4; i++)
    {
//        if (M3508s[i].OffLineFlag == 0)
//        { //�����ڸ�ֵ��ζ�����Ŷ�ȡ��һ�����ݵ������

            M3508s[i].targetSpeed = speed[i];
            speed[i] = Wheel_PID[i]->Incremental_PID(Wheel_PID[i], M3508s[i].targetSpeed, M3508s[i].realSpeed);
//        }
    }
		    for (int i = 0; i < 4; i++)
    {
        M3508s[i].outCurrent = speed[i];
    }


	
	
	
}


