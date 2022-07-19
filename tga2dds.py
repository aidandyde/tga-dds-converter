#Aidan Dyde T/A PlaneSimple 2022
from subprocess import check_output
import os

#Config - feel free to edit!

#DDS compression args. If you'd prefer to use dtx1 for example, you can set it here. See imagemagick documentation for mogrify for more info
magickArgs = "dds:mipmaps=1 -define dds:compression=dxt5"

#whether or not to keep the original tga files in the folder after conversion. True or False
keepOriginalFiles = False

#"GENERIC" or "TRANSPORT_FEVER_2" - I've made some specific refinements for tpf, but if you just want to use it as a general TGA>DDS converter you can
processMode = "TRANSPORT_FEVER_2"

#That's all, stop editing! Happy converting...

print("Welcome to the PlaneSimple TGA to DDS batch converter!")
print("Note: this script is Windows-only and requires imagick: https://imagemagick.org/index.php")

promptStr = "Please enter the base folder for the conversion, WITHOUT a trailing slash. (e.g. C:\\Users\\Me\\Documents"
if processMode == "TRANSPORT_FEVER_2":
    promptStr = "please paste the filepath to the res folder of your mod WITHOUT a trailing slash. (e.g. D:\\tpf_mods\\ivatt4\\ps_ivatt_4mt_1\\res) :"
baseFolder = input(promptStr)
#print(baseFolder)

for root, dirNames, fileNames in os.walk(baseFolder):
    #print(root)
    #print(fileNames)
    for fileName in fileNames:
        
        filePath = os.path.join(root, fileName)
        fileExtension = os.path.splitext(filePath)[1] #we don't care about the first output
        if fileExtension == ".tga":
            # excluding the TpF2 UI images, like ps_ivatt_4mt_br_latelogo_cblend@2x.tga, because I'm not sure they support DDS
            if processMode == "TRANSPORT_FEVER_2" and ("@" in fileName):
                continue
            cmd = "magick mogrify -format dds -define  " + magickArgs + " " + filePath
            print(cmd)
            print("converting "+fileName)
            check_output(cmd, shell=True) #this runs the command
            #remove the old .tga file
            if(not keepOriginalFiles):
                os.remove(filePath)
            
            

print("Loop finished. Please see the output above for any errors.")
