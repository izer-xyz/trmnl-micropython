#ifndef MICROPY_HW_BOARD_NAME
// Can be set by mpconfigboard.cmake.
#define MICROPY_HW_BOARD_NAME               "Seeed XIAO ESP32S3"
#endif
#define MICROPY_HW_MCU_NAME                 "ESP32-S3"

// Enable UART REPL for modules that have an external USB-UART and don't use native USB.
#define MICROPY_HW_ENABLE_UART_REPL         (1)

// REPL is on the native USB-CDC interface; the hardware UART is left free for
// the application. To put the REPL on UART0, define MICROPY_HW_ENABLE_UART_REPL.

#define MICROPY_HW_I2C0_SCL  (6)
#define MICROPY_HW_I2C0_SDA  (5)

#define MICROPY_HW_SPI1_MOSI (9)
#define MICROPY_HW_SPI1_MISO (8)
#define MICROPY_HW_SPI1_SCK  (7)
