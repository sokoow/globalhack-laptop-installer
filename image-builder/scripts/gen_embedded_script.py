#!/usr/bin/python3

import os
import sys
import json

################## TEMPLATES #################
IPXE_TEMPLATE = """#!ipxe
dhcp
#set net0/ip 192.168.1.125
#set net0/netmask 255.255.255.0
#set net0/gateway 192.168.30.1
#set dns 8.8.8.8

menu iPXE boot menu
item
item boot_from_disk           Boot from hard drive
{distro_items}
item boot_netbootxyz          Netboot.XYZ
item reboot_ipxe              Reboot iPXE Menu
item debug_ipxe               Debug  iPXE Network Connectivity
item
choose --default end --timeout 30000 target && goto ${{target}} || goto debug_ipxe
{distro_isolinux_cfg}

:boot_netbootxyz
chain --autofree https://boot.netboot.xyz/ipxe/netboot.xyz.lkrn

:boot_from_disk
echo "press any key to boot from hard drive"
sanboot --no-describe --drive 0x80

:debug_ipxe
#for ping/nslookup to work enable ping/nslookup command in config.h while buidling ipxe
echo "Interface Stat: net0"
ifstat net0
echo "Ping to gateway should work from here"
shell

:reboot_ipxe
echo "press any key to reboot"
exit
"""

ISOLINUX_CFG_TEMPLATE = """
:{target}
kernel {url}/{kernel} {kernel_args}
initrd {url}/{initrd}
boot
"""
################## TEMPLATES END #################

WORKDIR = os.path.split(os.path.realpath(sys.argv[1]))[0]

#config_file = 'gen_embedded.json'
config_file = os.path.split(os.path.realpath(sys.argv[1]))[1]

def load_config():
    with open(os.path.join(WORKDIR, config_file)) as load_fp:
        return json.load(load_fp)
DISTRO_INFO = load_config()

def render_isolinux_cfg():
    isolinux_cfgs = []
    for target, v in DISTRO_INFO.items():
        if v.get("kernel") and v.get("initrd"):
            kernel = v["kernel"]
            initrd = v["initrd"]
        else:
            if target.startswith("centos"):
                kernel = "vmlinuz"
                initrd = "initrd.img"
            elif target.startswith(("debian", "ubuntu")):
                kernel = "linux"
                initrd = "initrd.gz"

#        if kernel or initrd:
#            raise Exception(f"please add 'kernel' and 'initrd' (relative path against 'url') for the new distro in {config_file}")

        url = v["url"]
        answerfile = answerfile = v["answerfile"] if v.get("answerfile") else ""
        kernel_args = "{} {}".format(v["kernel_args"], answerfile)
        isolinux_cfgs.extend(ISOLINUX_CFG_TEMPLATE.format(**locals()))
    return "".join(isolinux_cfgs)


def main():
    distro_items = "\n".join(
        ["item {:25}{}".format(k, v["description"]) for k, v in DISTRO_INFO.items()]
    )
    distro_isolinux_cfg = render_isolinux_cfg()
    output = IPXE_TEMPLATE.format(**locals())
    output = output.replace("#CHANNEL", os.environ['CHANNEL'])
    output = output.replace("#ENDPOINT", os.environ['ENDPOINT'])
    dest = sys.argv[2] if len(sys.argv) == 3 else '.'
    if not os.path.exists(os.path.realpath(dest)):
        os.makedirs(os.path.realpath(dest))
    with open(os.path.join(os.path.realpath(dest), "boot.ipxe"), "w") as f:
        f.write(output)


if __name__ == "__main__":
    main()
