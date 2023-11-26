/**
 * @file Task_CanMsg.c
 * @author Miraggio (w1159904119@gmail)
 * @brief 
 * @version 0.1
 * @date 2021-03-30
 * 
 * @copyright Copyright (c) 2021
 * 
 */
#include "Task_CanMsg.h"
#include "BSP_CAN.h"
#include "DJI_C_IMU.h"
#include "M3508_Motor.h"
#include "M6020_Motor.h"

/**
  * @Data   2021-03-28	
  * @brief  can1接收任务
  * @param  void
  * @retval void
  */
void Can1Receives(void const *argument)
{
    Can_Export_Data_t Can_Export_Data;
    uint32_t ID;
    for (;;)
    {
        xQueueReceive(CAN1_ReceiveHandle, &Can_Export_Data, portMAX_DELAY);
        ID = Can_Export_Data.CAN_RxHeader.StdId;
        if (ID == M6020_READID_START)
        {
            M6020_Fun.M6020_getInfo(Can_Export_Data);
        }
        else if (ID >= M3508_READID_START || ID <= M3508_READID_END)
        {
            M3508_FUN.M3508_getInfo(Can_Export_Data);
        }
    }
}

/**
  * @Data   2021-03-28
  * @brief  can2接收任务
  * @param  void
  * @retval void
  */
void Can2Receives(void const *argument)
{
    uint32_t ID;
    Can_Export_Data_t Can_Export_Data;
    for (;;)
    {
        xQueueReceive(CAN2_ReceiveHandle, &Can_Export_Data, portMAX_DELAY);
        ID = Can_Export_Data.CAN_RxHeader.StdId;
         if (ID == DJI_C_Angle)
        {
            DJI_C_IMUFUN.DJI_C_Euler_getInfo(Can_Export_Data);
        }
        else if (ID == DJI_C_Gyro)
        {
            DJI_C_IMUFUN.DJI_C_Gyro_getInfo(Can_Export_Data);
        }
					else if(ID==M6020_READID_END)
		{
				M6020_Fun.M6020_getInfo(Can_Export_Data);
		}

				
				
    }
}
