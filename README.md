# net-programming
 Scripts for automating base config creation
 
 # Configlet Base
 Creates formatted and standardized text files for switch deployment using input from a spreadsheet. The output files are for:
 - to paste into the switch to get it online in cases where ZTP is not possible
 - Add to custom configlet in Cloudvision to configure DOWNLINK interfaces in cases where ESI is NOT used
 - To create the custom configlet that is added to CloudVision for the access layer switch uplinks
 - To create the custom configlets that are added to CloudVision for the access layer switch VLAN creation later have interface configuraitons

 Multiple switches can be run at once with one switch per worksheet within the spreadsheet creating all appropriate output files.

 # ArubaConfigGen
 Generates full Aruba 6300 (48 port switch) configuration. Uses the same input spreadsheet as the ConfigletBase. This configuration can be pasted into the switch and it's ready to go. Builds uplinks on port 1/1/51 and 1/1/52. Admin disables all other ports to later use the InterfaceDescription script to generate appropriate port configruations when everything is patched.

 # InterfaceDescription
 Creates formatted and standarized text files for switch port configurations based on input from a spreadsheet. The output can then be added to the appropriate custom configlet in CloudVision for the switch or pasted direcly into the switch. 
 
 The script customizes the switdchport configuraiton based on whether it is a standard data/phone access port, has a wireless AP connected, has a security devices or IOT specialty device.
 
 There are separate scripts for chassis based or fixed switches due to interface naming. Separate scripts for Arista or HP/Aruba.

 Multiple switches can be run at once with one switch per worksheet within the spreadsheet.
 
