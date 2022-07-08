from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk, configparser, serial
from serial import Serial
from serial import *

config = configparser.ConfigParser()
config.read('config_relay.ini')
config.sections()
com_port_relay = config['Config']['Com_port']
baud_rate = config['Config']['baud_rate']
int_baud_rate = int(baud_rate)
relay_on0 = 'relay on 0\r'
relay_on1 = 'relay on 1\r'
relay_on2 = 'relay on 2\r'
relay_on3 = 'relay on 3\r'
relay_on4 = 'relay on 4\r'
relay_on5 = 'relay on 5\r'
relay_on6 = 'relay on 6\r'
relay_on7 = 'relay on 7\r'
relay_off0 = 'relay off 0\r'
relay_off1 = 'relay off 1\r'
relay_off2 = 'relay off 2\r'
relay_off3 = 'relay off 3\r'
relay_off4 = 'relay off 4\r'
relay_off5 = 'relay off 5\r'
relay_off6 = 'relay off 6\r'
relay_off7 = 'relay off 7\r'
relay_read_all = 'relay readall\r'
relay_reset = 'reset\r'
write_all = 'relay writeall FF\r'

def exit():
    try:
        serPort.write(relay_reset.encode())
        serPort.close()
        screen.destroy()
    except:
        screen.destroy()


def reset():
    try:
        data_box.config(state='normal')
        data_box.delete('1.0', END)
        data_box.config(state='disable')
        serPort.write(relay_reset.encode())
        response_reset = serPort.read(20).decode()
        BT_on7['text'] = 'RELAY 7 OFF'
        BT_on7['background'] = '#E6E4E4'
        BT_on7['command'] = reverse_7
        BT_on6['text'] = 'RELAY 6 OFF'
        BT_on6['background'] = '#E6E4E4'
        BT_on6['command'] = reverse_6
        BT_on5['text'] = 'RELAY 5 OFF'
        BT_on5['background'] = '#E6E4E4'
        BT_on5['command'] = reverse_5
        BT_on4['text'] = 'RELAY 4 OFF'
        BT_on4['background'] = '#E6E4E4'
        BT_on4['command'] = reverse_4
        BT_on3['text'] = 'RELAY 3 OFF'
        BT_on3['background'] = '#E6E4E4'
        BT_on3['command'] = reverse_3
        BT_on2['text'] = 'RELAY 2 OFF'
        BT_on2['background'] = '#E6E4E4'
        BT_on2['command'] = reverse_2
        BT_on1['text'] = 'RELAY 1 OFF'
        BT_on1['background'] = '#E6E4E4'
        BT_on1['command'] = reverse_1
        BT_on0['text'] = 'RELAY 0 OFF'
        BT_on0['background'] = '#E6E4E4'
        BT_on0['command'] = reverse_0
        data_box.config(state='normal')
        data_box.insert(INSERT, response_reset)
        data_box.config(state='disable')
        BT_reset['state'] = 'disable'
    except:
        disable_button()
        messagebox_error()


def disable_button():
    BT_on0['state'] = 'disable'
    BT_on1['state'] = 'disable'
    BT_on2['state'] = 'disable'
    BT_on3['state'] = 'disable'
    BT_on4['state'] = 'disable'
    BT_on5['state'] = 'disable'
    BT_on6['state'] = 'disable'
    BT_on7['state'] = 'disable'
    BT_writeall['state'] = 'disable'
    BT_readall['state'] = 'disable'
    BT_reset['state'] = 'disable'


def disable_event():
    pass


def messagebox_error():
    BT_port['state'] = 'normal'
    BT_on7['text'] = 'RELAY 7 OFF'
    BT_on7['background'] = '#E6E4E4'
    BT_on6['text'] = 'RELAY 6 OFF'
    BT_on6['background'] = '#E6E4E4'
    BT_on5['text'] = 'RELAY 5 OFF'
    BT_on5['background'] = '#E6E4E4'
    BT_on4['text'] = 'RELAY 4 OFF'
    BT_on4['background'] = '#E6E4E4'
    BT_on3['text'] = 'RELAY 3 OFF'
    BT_on3['background'] = '#E6E4E4'
    BT_on2['text'] = 'RELAY 2 OFF'
    BT_on2['background'] = '#E6E4E4'
    BT_on1['text'] = 'RELAY 1 OFF'
    BT_on1['background'] = '#E6E4E4'
    BT_on0['text'] = 'RELAY 0 OFF'
    BT_on0['background'] = '#E6E4E4'
    messagebox.showerror('USB Error', '{} Not Found : Please insert USB and check the com port'.format(com_port_relay))


def reverse_7():
    BT_reset['state'] = 'normal'
    BT_on7['text'] = 'RELAY 7 ON'
    BT_on7['background'] = '#B6F9A1'
    BT_on7['command'] = antireverse_7
    try:
        serPort.write(relay_on7.encode())
        response_on7 = serPort.read(40).decode()
        data_box.config(state='normal')
        data_box.insert(INSERT, response_on7)
        data_box.config(state='disable')
    except:
        disable_button()
        messagebox_error()


def antireverse_7():
    BT_on7['text'] = 'RELAY 7 OFF'
    BT_on7['background'] = '#E6E4E4'
    BT_on7['command'] = reverse_7
    try:
        serPort.write(relay_off7.encode())
        response_off7 = serPort.read(40).decode()
        data_box.config(state='normal')
        data_box.insert(INSERT, response_off7)
        data_box.config(state='disable')
    except:
        disable_button()
        messagebox_error()


def reverse_6():
    BT_reset['state'] = 'normal'
    BT_on6['text'] = 'RELAY 6 ON'
    BT_on6['background'] = '#B6F9A1'
    BT_on6['command'] = antireverse_6
    try:
        serPort.write(relay_on6.encode())
        response_on6 = serPort.read(40).decode()
        data_box.config(state='normal')
        data_box.insert(INSERT, response_on6)
        data_box.config(state='disable')
    except:
        disable_button()
        messagebox_error()


def antireverse_6():
    BT_on6['text'] = 'RELAY 6 OFF'
    BT_on6['background'] = '#E6E4E4'
    BT_on6['command'] = reverse_6
    try:
        serPort.write(relay_off6.encode())
        response_off6 = serPort.read(40).decode()
        data_box.config(state='normal')
        data_box.insert(INSERT, response_off6)
        data_box.config(state='disable')
    except:
        disable_button()
        messagebox_error()


def reverse_5():
    BT_reset['state'] = 'normal'
    BT_on5['text'] = 'RELAY 5 ON'
    BT_on5['background'] = '#B6F9A1'
    BT_on5['command'] = antireverse_5
    try:
        serPort.write(relay_on5.encode())
        response_on5 = serPort.read(40).decode()
        data_box.config(state='normal')
        data_box.insert(INSERT, response_on5)
        data_box.config(state='disable')
    except:
        disable_button()
        messagebox_error()


def antireverse_5():
    BT_on5['text'] = 'RELAY 5 OFF'
    BT_on5['background'] = '#E6E4E4'
    BT_on5['command'] = reverse_5
    try:
        serPort.write(relay_off5.encode())
        response_off5 = serPort.read(40).decode()
        data_box.config(state='normal')
        data_box.insert(INSERT, response_off5)
        data_box.config(state='disable')
    except:
        disable_button()
        messagebox_error()


def reverse_4():
    BT_reset['state'] = 'normal'
    BT_on4['text'] = 'RELAY 4 ON'
    BT_on4['background'] = '#B6F9A1'
    BT_on4['command'] = antireverse_4
    try:
        serPort.write(relay_on4.encode())
        response_on4 = serPort.read(40).decode()
        data_box.config(state='normal')
        data_box.insert(INSERT, response_on4)
        data_box.config(state='disable')
    except:
        disable_button()
        messagebox_error()


def antireverse_4():
    BT_on4['text'] = 'RELAY 4 OFF'
    BT_on4['background'] = '#E6E4E4'
    BT_on4['command'] = reverse_4
    try:
        serPort.write(relay_off4.encode())
        response_off4 = serPort.read(40).decode()
        data_box.config(state='normal')
        data_box.insert(INSERT, response_off4)
        data_box.config(state='disable')
    except:
        disable_button()
        messagebox_error()


def reverse_3():
    BT_reset['state'] = 'normal'
    BT_on3['text'] = 'RELAY 3 ON'
    BT_on3['background'] = '#B6F9A1'
    BT_on3['command'] = antireverse_3
    try:
        serPort.write(relay_on3.encode())
        response_on3 = serPort.read(40).decode()
        data_box.config(state='normal')
        data_box.insert(INSERT, response_on3)
        data_box.config(state='disable')
    except:
        disable_button()
        messagebox_error()


def antireverse_3():
    BT_on3['text'] = 'RELAY 3 OFF'
    BT_on3['background'] = '#E6E4E4'
    BT_on3['command'] = reverse_3
    try:
        serPort.write(relay_off3.encode())
        response_off3 = serPort.read(40).decode()
        data_box.config(state='normal')
        data_box.insert(INSERT, response_off3)
        data_box.config(state='disable')
    except:
        disable_button()
        messagebox_error()


def reverse_2():
    BT_reset['state'] = 'normal'
    BT_on2['text'] = 'RELAY 2 ON'
    BT_on2['background'] = '#B6F9A1'
    BT_on2['command'] = antireverse_2
    try:
        serPort.write(relay_on2.encode())
        response_on2 = serPort.read(40).decode()
        data_box.config(state='normal')
        data_box.insert(INSERT, response_on2)
        data_box.config(state='disable')
    except:
        disable_button()
        messagebox_error()


def antireverse_2():
    BT_on2['text'] = 'RELAY 2 OFF'
    BT_on2['background'] = '#E6E4E4'
    BT_on2['command'] = reverse_2
    try:
        serPort.write(relay_off2.encode())
        response_off2 = serPort.read(40).decode()
        data_box.config(state='normal')
        data_box.insert(INSERT, response_off2)
        data_box.config(state='disable')
    except:
        disable_button()
        messagebox_error()


def reverse_1():
    BT_reset['state'] = 'normal'
    BT_on1['text'] = 'RELAY 1 ON'
    BT_on1['background'] = '#B6F9A1'
    BT_on1['command'] = antireverse_1
    try:
        serPort.write(relay_on1.encode())
        response_on1 = serPort.read(40).decode()
        data_box.config(state='normal')
        data_box.insert(INSERT, response_on1)
        data_box.config(state='disable')
    except:
        disable_button()
        messagebox_error()


def antireverse_1():
    BT_on1['text'] = 'RELAY 1 OFF'
    BT_on1['background'] = '#E6E4E4'
    BT_on1['command'] = reverse_1
    try:
        serPort.write(relay_off1.encode())
        response_off1 = serPort.read(40).decode()
        data_box.config(state='normal')
        data_box.insert(INSERT, response_off1)
        data_box.config(state='disable')
    except:
        disable_button()
        messagebox_error()


def reverse_0():
    BT_reset['state'] = 'normal'
    BT_on0['text'] = 'RELAY 0 ON'
    BT_on0['background'] = '#B6F9A1'
    BT_on0['command'] = antireverse_0
    try:
        data_box.config(state='normal')
        serPort.write(relay_on0.encode())
        response_on0 = serPort.read(40).decode()
        data_box.insert(INSERT, response_on0)
        data_box.config(state='disable')
    except:
        disable_button()
        messagebox_error()


def antireverse_0():
    BT_on0['text'] = 'RELAY 0 OFF'
    BT_on0['background'] = '#E6E4E4'
    BT_on0['command'] = reverse_0
    try:
        serPort.write(relay_off0.encode())
        response_off0 = serPort.read(40).decode()
        data_box.config(state='normal')
        data_box.insert(INSERT, response_off0)
        data_box.config(state='disable')
    except:
        disable_button()
        messagebox_error()


def connect_usb():
    global serPort
    try:
        data_box.config(state='normal')
        data_box.delete('1.0', END)
        serPort = serial.Serial(com_port_relay, int_baud_rate, timeout=0.5)
        data_box.insert(INSERT, '{} is connected..!!\n\n'.format(com_port_relay))
        data_box.config(state='disable')
        BT_on0['state'] = 'normal'
        BT_on1['state'] = 'normal'
        BT_on2['state'] = 'normal'
        BT_on3['state'] = 'normal'
        BT_on4['state'] = 'normal'
        BT_on5['state'] = 'normal'
        BT_on6['state'] = 'normal'
        BT_on7['state'] = 'normal'
        BT_writeall['state'] = 'normal'
        BT_readall['state'] = 'normal'
        BT_port['state'] = 'disable'
    except:
        messagebox_error()


def writeall():
    BT_reset['state'] = 'normal'
    try:
        serPort.write(write_all.encode())
        response_writeall = serPort.read(40).decode()
        BT_on7['text'] = 'RELAY 7 ON'
        BT_on7['background'] = '#B6F9A1'
        BT_on7['command'] = antireverse_7
        BT_on6['text'] = 'RELAY 6 ON'
        BT_on6['background'] = '#B6F9A1'
        BT_on6['command'] = antireverse_6
        BT_on5['text'] = 'RELAY 5 ON'
        BT_on5['background'] = '#B6F9A1'
        BT_on5['command'] = antireverse_5
        BT_on4['text'] = 'RELAY 4 ON'
        BT_on4['background'] = '#B6F9A1'
        BT_on4['command'] = antireverse_4
        BT_on3['text'] = 'RELAY 3 ON'
        BT_on3['background'] = '#B6F9A1'
        BT_on3['command'] = antireverse_3
        BT_on2['text'] = 'RELAY 2 ON'
        BT_on2['background'] = '#B6F9A1'
        BT_on2['command'] = antireverse_2
        BT_on1['text'] = 'RELAY 1 ON'
        BT_on1['background'] = '#B6F9A1'
        BT_on1['command'] = antireverse_1
        BT_on0['text'] = 'RELAY 0 ON'
        BT_on0['background'] = '#B6F9A1'
        BT_on0['command'] = antireverse_0
        data_box.config(state='normal')
        data_box.insert(INSERT, response_writeall)
        data_box.config(state='disable')
    except:
        disable_button()
        messagebox_error()


def readall():
    try:
        serPort.write(relay_read_all.encode())
        response_readall = serPort.read(40).decode()
        data_box.config(state='normal')
        data_box.insert(INSERT, response_readall)
        data_box.config(state='disable')
    except:
        disable_button()
        messagebox_error()


def main_screen():
    global BT_on0
    global BT_on1
    global BT_on2
    global BT_on3
    global BT_on4
    global BT_on5
    global BT_on6
    global BT_on7
    global BT_port
    global BT_readall
    global BT_reset
    global BT_writeall
    global data_box
    global frame
    global screen
    screen = Tk()
    screen.resizable(0, 0)
    screen.protocol('WM_DELETE_WINDOW', disable_event)
    screen.configure(bg='#FEBA87')
    screen.geometry('535x500+320+75')
    screen.title('USB Relay 8 Channel Controller V1.0')
    headname = tk.Label(screen, text='USB Relay 8 Channel Controller V1.0', font='Arial 18 bold')
    headname.pack(pady=10, ipadx=15, ipady=5)
    style = ttk.Style(screen)
    style.configure('TFrame')
    frame = ttk.Frame(screen, style='TFrame')
    frame.pack(ipady=10, pady=5)
    style2 = ttk.Style(screen)
    style2.configure('Bold.TButton', font=('Arial', '9', 'bold'))
    BT_port = ttk.Button(screen, text=' Connect\nUSB Port', style='Bold.TButton', command=connect_usb)
    BT_port.place(x=15, y=155, height=45, width=100)
    port_pic = PhotoImage(file='port.png')
    BT_port.config(image=port_pic, compound=(tk.LEFT))
    BT_exit = ttk.Button(screen, text=' EXIT', style='Bold.TButton', command=exit)
    BT_exit.place(x=15, y=215, height=45, width=100)
    exit_pic = PhotoImage(file='exit_relay.png')
    BT_exit.config(image=exit_pic, compound=(tk.LEFT))
    BT_reset = ttk.Button(screen, text='RESET', style='Bold.TButton', command=reset, state='disable')
    BT_reset.place(x=420, y=255, height=45, width=100)
    reset_pic = PhotoImage(file='reset.png')
    BT_reset.config(image=reset_pic, compound=(tk.LEFT))
    BT_writeall = ttk.Button(screen, text='   RELAY\nWriteall FF', style='Bold.TButton', command=writeall, state='disable')
    BT_writeall.place(x=420, y=145, height=45, width=100)
    writeall_pic = PhotoImage(file='write_all.png')
    BT_writeall.config(image=writeall_pic, compound=(tk.LEFT))
    BT_readall = ttk.Button(screen, text=' RELAY\nReadall', style='Bold.TButton', command=readall, state='disable')
    BT_readall.place(x=420, y=200, height=45, width=100)
    readall_pic = PhotoImage(file='readall.png')
    BT_readall.config(image=readall_pic, compound=(tk.LEFT))
    BT_on7 = Button(frame, text='RELAY 7 OFF', bg='#E6E4E4', command=reverse_7, state='disable')
    BT_on7.grid(row=0, column=0, padx=25, pady=10, ipadx=7, ipady=10)
    BT_on0 = Button(frame, text='RELAY 0 OFF', bg='#E6E4E4', command=reverse_0, state='disable')
    BT_on0.grid(row=0, column=1, padx=25, pady=10, ipadx=7, ipady=10)
    BT_on6 = Button(frame, text='RELAY 6 OFF', bg='#E6E4E4', command=reverse_6, state='disable')
    BT_on6.grid(row=1, column=0, padx=25, pady=10, ipadx=7, ipady=10)
    BT_on1 = Button(frame, text='RELAY 1 OFF', bg='#E6E4E4', command=reverse_1, state='disable')
    BT_on1.grid(row=1, column=1, padx=25, pady=10, ipadx=7, ipady=10)
    BT_on5 = Button(frame, text='RELAY 5 OFF', bg='#E6E4E4', command=reverse_5, state='disable')
    BT_on5.grid(row=2, column=0, padx=25, pady=10, ipadx=7, ipady=10)
    BT_on2 = Button(frame, text='RELAY 2 OFF', bg='#E6E4E4', command=reverse_2, state='disable')
    BT_on2.grid(row=2, column=1, padx=25, pady=10, ipadx=7, ipady=10)
    BT_on4 = Button(frame, text='RELAY 4 OFF', bg='#E6E4E4', command=reverse_4, state='disable')
    BT_on4.grid(row=3, column=0, padx=25, pady=10, ipadx=7, ipady=10)
    BT_on3 = Button(frame, text='RELAY 3 OFF', bg='#E6E4E4', command=reverse_3, state='disable')
    BT_on3.grid(row=3, column=1, padx=25, pady=10, ipadx=7, ipady=10)
    data_box = Text(screen, width=40, height=8, font='Arial 10')
    data_box.pack(pady=5)
    data_box.config(state='disable')
    yscrollbar = ttk.Scrollbar(screen, command=(data_box.yview))
    yscrollbar.place(x=408, y=364, height=132)
    data_box['yscrollcommand'] = yscrollbar.set
    screen.mainloop()


main_screen()
