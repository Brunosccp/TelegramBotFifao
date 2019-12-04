import csv
from converter import Converter

class CSVReader:

    enum = Converter()

    def getXTest(self):
        with open('data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            trainingDataset = []
            
            for row in csv_reader:
                if line_count == 0:
                    #print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    try: 
                        overall = int(row[7])
                        age = int(row[3])
                        position = self.enum.convertPosition(row[21])
                        preferredFoot = self.enum.convertPreferredFoot(row[14])
                    except ValueError:
                        continue

                    player = [overall, age, position, preferredFoot]
                    
                    trainingDataset.append(player)
                    #print(f'parametro: {row[16]}')
                    line_count += 1
            print(f'Processed {line_count} lines.')

            return trainingDataset
    
    def getYTest(self):
        with open('data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0

            trainingDataset = []
            
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    rawValue = row[11]
                    value = self.enum.convertValue(rawValue)

                    trainingDataset.append(value)
                    line_count += 1
            print(f'Processed {line_count} lines.')

            return trainingDataset