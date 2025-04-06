#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/timer.h"
#include "pico/cyw43_arch.h"

bool led_val;

int64_t alarm_callback(alarm_id_t id, void *user_data) {
    // Put your timeout handler code in here
    led_val = cyw43_arch_gpio_get(CYW43_WL_GPIO_LED_PIN);
    cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, led_val? 0 : 1);
    return 1000000;
}




int main()
{
    stdio_init_all();

    // Initialise the Wi-Fi chip
    if (cyw43_arch_init()) {
        printf("Wi-Fi init failed\n");
        return -1;
    }

    // Timer example code - This example fires off the callback after 2000ms
    add_alarm_in_ms(1000, alarm_callback, NULL, false);
    // For more examples of timer use see https://github.com/raspberrypi/pico-examples/tree/master/timer
    //add_repeating_timer_ms(1000, alarm_callback, NULL, NULL);
    // Example to turn on the Pico W LED
    cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 1);

    while (true) {
        printf("Hello, world!\n");
        sleep_ms(1000);
    }
}
