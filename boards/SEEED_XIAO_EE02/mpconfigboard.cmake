include(boards/ESP32_GENERIC_S3/mpconfigboard.cmake)

list(APPEND SDKCONFIG_DEFAULTS
    boards/sdkconfig.flash_qio_80m
    boards/sdkconfig.240mhz
    boards/sdkconfig.spiram_oct
    ${MICROPY_BOARD_DIR}/sdkconfig.board
)

set(MICROPY_FROZEN_MANIFEST ${MICROPY_BOARD_DIR}/manifest.py)
