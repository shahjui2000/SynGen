import os
import sys

mainfolder = str(sys.argv[1])
print ('Your folder(containing images) path:' + mainfolder)

if (len(sys.argv)> 2 ):
 print('Usage details: fig_latex.py <input1>')
 sys.exit

files = os.listdir(mainfolder)

f = open(os.path.join(mainfolder,"includegraphics_text.txt"), "w")

print('#####################################')
for i in range(len(files)):
    print('Loop running for:'+ os.path.join(mainfolder,files[i]))
    f.write('\\begin'+str('{')+'figure'+str('}')+'[H] \n \t \includegraphics[width =0.5\\textwidth]{' +files[i]+'} \n \end'+str('{')+'figure'+str('}')+'\n\n')

f.close()
print('#####################################')
print('Text File saved in the same folder')