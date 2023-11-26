/**
 * @file Task_CanSend.h
 * @author Miraggio (w1159904119@gmail)
 * @brief 
 * @version 0.1
 * @date 2021-05-31
 * 
 * @copyright Copyright (c) 2021
 * 
 */
#ifndef __TASK_CANSEND_H
#define __TASK_CANSEND_H
#include "BSP_CAN.h"
//#include "typedef.h"
extern osMessageQId CAN1_ReceiveHandle;
extern osMessageQId CAN2_ReceiveHandle;
extern osMessageQId CAN_SendHandle;


void AllCanSend(void const *argument);

#endif

