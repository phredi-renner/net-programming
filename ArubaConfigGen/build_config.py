##########################################################
# Uses input from spreadsheet to create a configuration 
# to be pasted into Aruba 6300 swtich. 
# 
# 
#
# Created by: Fred Renner
# Date: 5/2/2023
# Version: 1.0
##########################################################

import jinja2
import openpyxl
from jinja2 import Environment, FileSystemLoader

# Gather some info
work = input('Enter spreadsheet filename: ')
wkbk = 'input/'+work+'.xlsx'

# Defines the templates
environment = Environment(loader=FileSystemLoader("templates/"))
a6300_template = environment.get_template("6300_config.j2")

# Open the spreadsheet where we have the data
wb = openpyxl.load_workbook(wkbk)

# Here we will look at each worksheet and gather the information
for sheet in wb.sheetnames:
    # Grab all the variable data from the spreadsheet
    page = wb[sheet]
    bldg = page['B1'].value
    floor = page['B2'].value
    sw_num = page['B3'].value
    mgt_vlan = page['B5'].value
    mgt_ip = page['B6'].value
    mgt_msk = page['B7'].value
    mgt_gw = page['B8'].value
    pc_num = page['B9'].value
    lf_int1 = page['B10'].value
    lf_int2 = page['B11'].value
    up_int1 = page['B13'].value
    up_int2 = page['B14'].value
    d_vlan = page['B16'].value
    v_vlan = page['B17'].value
    sec_vlan = page['B18'].value
    sp_vlan = page['B19'].value
    vrf = page['B22'].value
    # Create some variables we will use based on the info in the spreadsheet
    hostname = 'wb-us-bur-b'+ str(bldg) +'f' + str(floor) + '-as' + str(sw_num)
    dyn_config_outfile = 'dyn_config_' + str(hostname) + '_' + str(mgt_ip)
    
    # Define the output files and location, these are just text files. I like the .ios
    # extension for color formatting.
    filename1  = dyn_config_outfile + '.ios'
    out_dir = 'output/'

    # Create the files based on the appropriate templates
    f1content = a6300_template.render(
        page=page,
        bldg=bldg,
        floor=floor,
        sw_num=sw_num,
        mgt_vlan=mgt_vlan,
        mgt_ip=mgt_ip,
        mgt_msk=mgt_msk,
        mgt_gw=mgt_gw,
        pc_num=pc_num,
        lf_int1=lf_int1,
        lf_int2=lf_int2,
        up_int1=up_int1,
        up_int2=up_int2,
        d_vlan=d_vlan,
        v_vlan=v_vlan,
        sec_vlan=sec_vlan,
        sp_vlan=sp_vlan,
        vrf=vrf,
        hostname=hostname,
    )

# Write the files and display the filenames
    with open(out_dir+filename1, mode="w", encoding="utf-8") as message:
        message.write(f1content)
    print(f"... wrote {filename1}")