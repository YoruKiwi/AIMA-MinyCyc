import serial
import serial.tools.list_ports


def get_serial_list():
    """
    Returns a list of available serial ports.

    Returns:
        list: A list of available serial ports.
    """
    ports = serial.tools.list_ports.comports()
    available_ports = []
    for port in ports:
        available_ports.append(port.device)
    return available_ports
# © AIMA DEVELOPPEMENT 2024