import os

class SVG:
    def __init__(self,fill): 
        self.fill = fill
        self.SVGs = {}
        files = os.listdir('./Resources')
        for file in files:
            if file.endswith('.svg'):
                svgFile = open('./Resources/'+file,'r')
                svg = svgFile.readline()
                self.SVGs[file] = svg
                svgFile.close()
                
                if 'fill' not in svg:
                    index = svg.find("<path")
                    if index != -1:
                        modified_string = svg[:index + len("<path")] + f' fill = "#{self.fill}" ' + svg[index + len("<path"):]
                        svgFile = open('./Resources/'+file,'w')
                        svgFile.write(modified_string)
                        svgFile.close()

                else:
                    new_string = svg.replace('fill = "#' + svg.split('fill = "#')[1].split()[0], 'fill = "#' + self.fill+'"')
                    svgFile = open('./Resources/'+file,'w')
                    svgFile.write(new_string)
                    svgFile.close()

    def changeColour(self,newFill):
        self.fill = newFill
        for file in self.SVGs:
            svgFile = open('./Resources/'+file,'r')
            svg = svgFile.readline()
            self.SVGs[file] = svg
            svgFile.close()

            new_string = svg.replace('fill = "#' + svg.split('fill = "#')[1].split()[0], 'fill = "#' + self.fill+'"')
            svg = open('./Resources/'+file,'w')
            svg.write(new_string)
            svg.close()