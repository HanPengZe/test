/**
 * @file Task_CanMsg.h
 * @author Miraggio (w1159904119@gmail)
 * @brief 
 * @version 0.1
 * @date 2021-03-30
 * 
 * @copyright Copyright (c) 2021
 * 
 */
#ifndef __TASK_CANMSG_H
#define __TASK_CANMSG_H
#include "BSP_CAN.h"

extern osMessageQId CAN1_ReceiveHandle;
extern osMessageQId CAN2_ReceiveHandle;
extern osMessageQId CAN_SendHandle;

enum
{
    M6020 = 0,      /* 6020���� */
    M3508,          /* 3508���� */
    M3508_Friction, /* 3508��Ħ���֣����� */
    M2006,          /* 2006���� */
    Wolf_IMU,       /* ��������ǽ��� */
    DJI_IMU,        /* C�������ǽ��� */
};

void Can1Receives(void const *argument);
void Can2Receives(void const *argument);

#endif /*__TASK_CANMSG_H*/
