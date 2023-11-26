#ifndef __BSP_CAN
#define __BSP_CAN

#include "can.h"
#include "cmsis_os.h"
#include "queue.h"
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#define Can1_Type 1
#define Can2_Type 2

#define Can_FunGroundInit               \
    {                                   \
        &CAN_IT_Init,                   \
            &CAN_RxMessage_Export_Date, \
            &CAN_SendData,              \
            &Check_CAN,                 \
    }

#define Can_DataGroundInit \
    {                      \
        {0}, {0},          \
    }
		#pragma anon_unions

/*************CAN对外数据接口************/
typedef struct
{
    CAN_RxHeaderTypeDef CAN_RxHeader;
    uint8_t CANx_Export_RxMessage[8];
} Can_Export_Data_t;

/*************CAN发送数据接口************/
typedef struct
{
    CAN_HandleTypeDef *Canx;
    CAN_TxHeaderTypeDef CAN_TxHeader;
    uint8_t CANx_Send_RxMessage[8];
} Can_Send_Data_t;


typedef struct
{
    struct
    {
        CAN_FilterTypeDef CAN_Filter;
    } CAN_FilterTypedef;

    struct
    {
        CAN_RxHeaderTypeDef CANx_RxHeader;
        uint8_t CAN_RxMessage[8];
    } CAN_RxTypedef;

} Can_Data_t;

typedef struct
{
    void (*CAN_IT_Init)(CAN_HandleTypeDef *hcanx, uint8_t Can_type);
    void (*CAN_RxMessage_Export_Date)(CAN_HandleTypeDef *hcanx, osMessageQId CANx_Handle, uint8_t Can_type);
    void (*CAN_SendData)(osMessageQId CANx_Handle, CAN_HandleTypeDef *CANx, uint8_t id_type, uint32_t id, uint8_t data[8]);
    void (*Check_CAN)(void);
} Can_Fun_t;

typedef struct
{
    uint8_t InfoUpdateFlag;   //信息读取更新标志
    uint16_t InfoUpdateFrame; //帧率
    uint8_t OffLineFlag;      //离线故障标志
} CAN_Devices_t;

extern CAN_Devices_t Monitor_CAN1, Monitor_CAN2;
extern Can_Fun_t Can_Fun;

#endif /*__BSP_CAN*/

