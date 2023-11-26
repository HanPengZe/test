#ifndef __CLOUD_H
#define __CLOUD_H
#define CAN_GIMBAL_ALL_ID  		0x1FF
#define M6020_MaxOutput 30000 //发送给电机的最大控制值
#include <stdint.h>

typedef struct 
{
	float NowYaw;
	float TargetYaw;
	float In_Put;
	float Out_Put;
	float NowPitch;
	float TargetPitch;
	
}Cloud_t;
#define YawAttitude_PIDInit    \
    {                          \
        0,                     \
            0,                 \
            0,                 \
            0,                 \
            0,                 \
            100,             \
            0.0f,              \
            10,              \
            0,                 \
            0,                 \
            0,                 \
            0,                 \
            10000,             \
            0,                 \
            0,                 \
            &Cloud_IMUYAWOPID, \
    }//云台陀螺仪外环PID初始化
#define YawSpeed_PIDInit       \
    {                          \
        0,                     \
            0,                 \
            0,                 \
            0,                 \
            0,                 \
            6,             \
            0.0f,              \
            10,              \
            0,                 \
            0,                 \
            0,                 \
            0,                 \
            10000,   \
            1000,              \
            15000,             \
            &Cloud_IMUYAWIPID, \
    }//云台陀螺仪PID内环初始化
#define M6020s_PitchOPIDInit  \
    {                         \
        0,                    \
            0,                \
            0,                \
            0,                \
            0,                \
            0.35f,            \
            0.0f,             \
            0.f,             \
            0,                \
            0,                \
            0,                \
            0,                \
            500,              \
            0,                \
            3000,             \
            &Cloud_PITCHOPID, \
    }
#define M6020s_PitchIPIDInit  \
    {                         \
        0,                    \
            0,                \
            0,                \
            0,                \
            0,                \
            50.0f,           \
            0.f,             \
            0.0f,             \
            0,                \
            0,                \
            0,                \
            0,                \
            15000,  \
            30,               \
            4000,             \
            &Cloud_PITCHIPID, \
    }


extern Cloud_t Cloud_Yaw;
extern Cloud_t Cloud_Pitch;

//void CAN_cmd_gimbal(int16_t yaw, int16_t pitch, int16_t shoot, int16_t rev);
//void Cloud_Init(void);
void Cloud_Yaw_PID(int16_t yaw);
void Cloud_Pitch_PID(int16_t pitch);

void cloud_Mpu(void);
//void PID_Init(void);













#endif
