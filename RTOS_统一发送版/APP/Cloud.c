#include "Cloud.h"
#include "PID.h"
#include "DJI_C_IMU.h"
#include "M6020_Motor.h"

Cloud_t Cloud_Yaw;
Cloud_t Cloud_Pitch;

positionpid_t YawAttitude_PID = YawAttitude_PIDInit; //�⻷��̨yaw����̬pid
positionpid_t YawSpeed_PID = YawSpeed_PIDInit; //�ڻ���̨yaw���ٶ�pid

positionpid_t M6020s_PitchOPID = M6020s_PitchOPIDInit; //PITCH����̨����⻷
#undef M6020s_PitchOPIDInit
positionpid_t M6020s_PitchIPID = M6020s_PitchIPIDInit; //PITCH����̨����ڻ�
#undef M6020s_PitchIPIDInit


 
void cloud_Mpu(void)
{

	Cloud_Yaw .TargetYaw=DJI_C_IMU.total_yaw;
	Cloud_Pitch. TargetPitch=DJI_C_IMU.pitch;
}


void Cloud_Yaw_PID(int16_t yaw)
{
	Cloud_Yaw .NowYaw=DJI_C_IMU.total_yaw;
	Cloud_Yaw .TargetYaw+=yaw*0.001;//�ۼ�Ŀ��Ƕȣ�����ȡ����Ŀ��Ƕȣ������һֱ�ص�0�ĽǶȣ�
	Cloud_Yaw .In_Put=YawAttitude_PID.Position_PID(&YawAttitude_PID, Cloud_Yaw .TargetYaw, Cloud_Yaw .NowYaw);//λ�û����⻷
	Cloud_Yaw .Out_Put = YawSpeed_PID.Position_PID(&YawSpeed_PID, YawAttitude_PID.pwm, DJI_C_IMU.Gyro_z);//�ڻ�
}
void Cloud_Pitch_PID(int16_t pitch)
{
	Cloud_Pitch .NowPitch=DJI_C_IMU.pitch;
	Cloud_Pitch  .TargetPitch+=pitch*0.01;
	if(Cloud_Pitch  .TargetPitch<=-900)
	{
		Cloud_Pitch  .TargetPitch=-900;
	}
	else if(Cloud_Pitch  .TargetPitch>=780)
	{
		Cloud_Pitch  .TargetPitch=780;
	}
	      Cloud_Pitch .In_Put=M6020s_PitchOPID.Position_PID(&M6020s_PitchOPID,Cloud_Pitch.TargetPitch,Cloud_Pitch .NowPitch );
        Cloud_Pitch.Out_Put= M6020s_PitchIPID.Position_PID(&M6020s_PitchIPID, M6020s_PitchOPID.pwm, M6020s_Pitch.realSpeed);

}




