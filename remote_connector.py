import pexpect
import argparse


parser = argparse.ArgumentParser(description='Remote Connector')

# config of stepping machine
parser.add_argument('--step_usr', default='XXX', type=str, help='user name of stepping machine')
parser.add_argument('--step_pwd', default='YYY', type=str, help='password of stepping machine')
parser.add_argument('--step_ip', default='ZZZ', type=str, help='ip of stepping machine')
parser.add_argument('--step_port', default='22079', type=str, help='port of stepping machine')

# config of target machine
parser.add_argument('--target_ip', default='192.168.124.27', type=str, help='ip of target machine')
parser.add_argument('--target_port', default='22', type=str, help='ip of target machine')

# config of local port
parser.add_argument('--local_port', default='6002', type=str, help='local port')

args = parser.parse_args()

cmd = 'ssh -L {}:{}:{} -p {} {}@{}'.format(args.local_port, args.target_ip, args.target_port, args.step_port, args.step_usr, args.step_ip)

print("Your command: {}".format(cmd))

child = pexpect.spawn(cmd)
index = child.expect('password')
print('index:{}'.format(index))

if index == 0:
    print("Typing password automatically ...")
    child.sendline(args.pwd) # password of stepping machine 
    child.expect(pexpect.EOF, timeout=None)
else:
    print("Failed to connect ...")

# ssh -p 6002 target_machine_user_name@loaclhost
# target machie password
