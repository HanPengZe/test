#include "Task_Sampling.h"
#include "DJI_C_IMU.h"
#include "Robot_control.h"
#include "Cloud.h"



void Fixed_Sampling(void const *argument)
{
	static uint8_t mark=0;
    portTickType xLastWakeTime;
    xLastWakeTime = xTaskGetTickCount();

    const TickType_t TimeIncrement = pdMS_TO_TICKS(2); //每一毫秒强制进入总控制

    for (;;)
    {
			
			
    DJI_C_IMUFUN.Updata_Hand_Euler_Gyro_Data();
		if(mark==0)
		{
			cloud_Mpu();
			mark=1;
		}
		Robot_control();
		


        vTaskDelayUntil(&xLastWakeTime, TimeIncrement);
    }
}
