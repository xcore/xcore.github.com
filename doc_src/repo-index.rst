Repository index
----------------

Below is a list of repositories, roughly classified by purpose. Some
repositories are in a class of their own and are, until other similar
repositories appear, held in a *miscellaneous* category. These categories
are necessarily crude, and will hopefully improve over time.

- Software components and applications that execute on an XCore:

  - I/O:

    - *Serial interfaces* such as SPI, UART, JTAG, ...

    - *Analogue interfaces* such as PWM

    - *Memory interfaces* such as SDRAM, FRAM, SD Card

  - *Networking* such as USB, Ethernet

  - *Numerical* fixed point, DSP, filters, transforms

  - *Unclassified applications* Miscellaneous applications.

- *Boards* standard software on boards.

- *Tools* compilers, debuggers, probing

- *Documents* 

- *Infrastructure* needed for any or some of the above.

In the table below, we list the repositories, a short description,
which license they use (XOSL is the XMOS open source license), and
whether they use the standard build structure from xcommon (sc_, sw_) or xdoc (doc_).

+-----------------+----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|Class            | Repository                                                                 | Purpose                                                   | Lic   | build  |
+-----------------+----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|Serial intfcs    | `sc_jtag <http://github.com/xcore/sc_jtag>`_                               | JTAG communication protocols                              | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_spdif <http://github.com/xcore/sc_spdif>`_                             | S/PDIF TX and RX component                                | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_adat <http://github.com/xcore/sc_adat>`_                               | ADAT TX and RX component                                  | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_spi <http://github.com/xcore/sc_spi>`_                                 | SPI Master/Slave Software Component                       | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_uart <http://github.com/xcore/sc_uart>`_                               | UART Components                                           | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_i2c <http://github.com/xcore/sc_i2c>`_                                 | Generic I2C support                                       | XOSL  | xcommon|
+-----------------+----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|Analogue intfcs  | `sc_class_d_amplifier <http://github.com/xcore/sc_class_d_amplifier>`_     | Class D amplifier                                         | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_pwm <http://github.com/xcore/sc_pwm>`_                                 | Pulse Width Modulation (PWM) components                   | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_capacitive_sensing <http://github.com/xcore/sc_capacitive_sensing>`_   | Capacitive sensing (capsens) on an XCore                  | XOSL  | xcommon|
+-----------------+----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|Memory intfcs    | `sc_sdram <http://github.com/xcore/sc_sdram>`_                             | SDRAM controller                                          | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_sdcard <http://github.com/xcore/sc_sdcard>`_                           | SD Card interface                                         | XOSL  | no     |
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_fram_if <http://github.com/xcore/sc_fram_if>`_                         | A lightweight SPI F-RAM interface.                        | XOSL  | xcommon|
+-----------------+----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|Networking       | `sc_usb <http://github.com/xcore/sc_usb>`_                                 | USB device library                                        | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_ethernet <http://github.com/xcore/sc_ethernet>`_                       | 10/100 Mii Ethernet mac and filters                       | ?     | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_xtcp <http://github.com/xcore/sc_xtcp>`_                               | micro TCP/IP stack for use with sc_ethernet               | ?     | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_ethercat <http://github.com/xcore/sc_ethercat>`_                       | Feasibility study of EtherCAT                             | XOSL  | xcommon|
+-----------------+----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|Numerical        | `sw_par_audio_dsp <http://github.com/xcore/sw_par_audio_dsp>`_             | Parallel Audio DSP example                                | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_dsp_filters <http://github.com/xcore/sc_dsp_filters>`_                 | Standard DSP filters, such as Biquads and FIRs            | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_dsp_transforms <http://github.com/xcore/sc_dsp_transforms>`_           | DSP transforms, such as DCT.                              | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_lib_fixed_point <http://github.com/xcore/sc_lib_fixed_point>`_         | A library for manipulating 8.24 fixed point numbers.      | XOSL  | xcommon|
+-----------------+----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|Unclassified     | `sw_led_tile_controller <http://github.com/xcore/sw_led_tile_controller>`_ | LED Tile Controller                                       | XOSL  | xcommon|
|apps             +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sw_avb <http://github.com/xcore/sw_avb>`_                                 | AVB Audio Video Bridge implementation (IEEE 1722)         | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sw_pintest <http://github.com/xcore/sw_pintest>`_                         | Application for testing pin connectivity                  | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_crypto <http://github.com/xcore/sc_crypto>`_                           | Cryptographic algorithms for the XCore                    | XOSL  | xcommon|
+-----------------+----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|Hardware         | `proj_shift_registers <http://github.com/xcore/proj_shift_registers>`_     | Shift register board                                      | XOSL  | no     |
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `proj_xmp64 <http://github.com/xcore/proj_xmp64>`_                         | Project repository for the XMP 64 multiprocessor board    | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `proj_xtag2 <http://github.com/xcore/proj_xtag2>`_                         | XTAG2 hardware and software                               | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `hw_slicekit_system <http://github.com/xcore/hw_slicekit_system>`_         | Specifications for Modular Development Hardware           | XOSL  | no     |
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `hw_l1_48_module <http://github.com/xcore/hw_l1_48_module>`_               | 3V3 powered DIL module with a 48 pin device               | XOSL  | N/A    |
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `xmos_kicad_parts <https://github.com/topiaruss/xmos_kicad_parts>`_        | KiCAD schematics and footprints for L1-128 and L1-64      | ?     | N/A    |
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sw_xk1_examples <http://github.com/xcore/sw_xk1_examples>`_               | XK-1 example applications                                 | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sw_xc1_examples <http://github.com/xcore/sw_xc1_examples>`_               | XC-1 example applications                                 | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sw_xc1a_examples <http://github.com/xcore/sw_xc1a_examples>`_             | XC-1A example applications                                | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sw_xc2_examples <http://github.com/xcore/sw_xc2_examples>`_               | XC-2 example applications                                 | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sw_xdk_examples <http://github.com/xcore/sw_xdk_examples>`_               | XDK example applications                                  | XOSL  | xcommon|
+-----------------+----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|Tools            | `tool_sire <http://github.com/xcore/tool_sire>`_                           | Language and runtime system for dynamic process creation  | XOSL  | N/A    |
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `dis-xs1 <http://git.infradead.org/users/segher/dis-xs1.git>`_             | XS1 Disassembler, Assembler, XC-1A JTAG tools             | GPL   | N/A    |
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `tool_pyxsim <http://github.com/xcore/tool_pyxsim>`_                       | Python wrapper for the XMOS simulator testbench           | XOSL  | N/A    |
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_xlog <http://github.com/xcore/sc_xlog>`_                               | Logging component                                         | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_lib_xscope <http://github.com/xcore/sc_lib_xscope>`_                   | Device side xscope library                                | XOSL  | no     |
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sw_xscope_examples <http://github.com/xcore/sw_xscope_examples>`_         | Examples on how to use the xscope tracing library         | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `libusb <http://github.com/mattfyles/xmos_libusb_binaries.git>`_           | Host-side USB library                                     | LGPL  | N/A    |
+-----------------+----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|Documents        | `doc_tips_and_tricks <http://github.com/xcore/doc_tips_and_tricks>`_       | Various tricks on how to program an XS1                   | XOSL  | xdoc   |
+-----------------+----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|Infrastructure   | `xcommon <http://github.com/xcore/xcommon>`_                               | Common application framework for XMOS software            | XOSL  | -      |
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `xdoc <http://github.com/xcore/xdoc>`_                                     | Common infrastructure for code documentation              | XOSL  | -      |
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `xcore.github.com <http://github.com/xcore/xcore.github.com>`_             | Community web stuff, in HTML                              | XOSL  | xdoc   |
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `Community <http://github.com/xcore/Community>`_                           | Community web stuff and documentation (contains this list)| XOSL  | -      |
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `sc_lib_example <http://github.com/xcore/sc_lib_example>`_                 | Example module how to make an exportable binary library   | XOSL  | xcommon|
|                 +----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+
|                 | `xcore_template <http://github.com/xcore/xcore_template>`_                 | A template for a sc repository module                     | XOSL  | xcommon|
+-----------------+----------------------------------------------------------------------------+-----------------------------------------------------------+-------+--------+

