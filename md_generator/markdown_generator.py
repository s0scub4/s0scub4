import os
import pandas

def save_in_md_format(data):
#     EXAMPLE:
#
# ---
# layout: post
# title: Video 1
# category: represion
# tags: artemisa
# date: 2021-07-13
# ---
#
# Lorem, ipsum dolor sit amet consectetur adipisicing elit. Molestias aut, repellat ipsum facere voluptate dicta 
# <iframe width="420" height="315" src="http://www.youtube.com/embed/pP9Bto5lOEQ" frameborder="0" allowfullscreen></iframe>
#

# <div> class="wise-iframe-wrapper"><iframe width="730" height="548" src="https://www.youtube.com/embed/6vU7SzCdpuM" allowfullscreen></iframe></div>

    for i in range(len(data)):
        filename = data.iloc[i]['date'] + '-' + data.iloc[i]['title'] + '.md'
        try:
            with open('../md_file/'+filename, 'w') as file:
                file.write('---\n')
                
                file.write('layout: %s\n'                % data.iloc[i]['layout'])
                file.write('title: %s\n'                 % data.iloc[i]['title'])
                file.write('category: %s\n'              % data.iloc[i]['category'])
                file.write('tags: %s\n'                  % data.iloc[i]['tags'])
                file.write('date: %s\n'                  % data.iloc[i]['date'])

                file.write('---\n')

                file.write('\n')
                file.write('%s\n'                        % data.iloc[i]['text'])
                file.write('\n')

                location = '<div class="wise-iframe-wrapper"><iframe width="730" height="548" src="'+ data.iloc[i]['location'] +'" allowfullscreen></iframe></div>'
                file.write('%s\n'                        % location)
            file.close()

        except:
            os.mkdir('../md_file/')
            with open('../md_file/'+filename, 'w') as file:
                file.write('---\n')

                file.write('layout: %s\n'                % data.iloc[i]['layout'])
                file.write('title: %s\n'                 % data.iloc[i]['title'])
                file.write('category: %s\n'              % data.iloc[i]['category'])
                file.write('tags: %s\n'                  % data.iloc[i]['tags'])
                file.write('date: %s\n'                  % data.iloc[i]['date'])

                file.write('---\n')
                
                file.write('\n')
                file.write('%s\n'                        % data.iloc[i]['text'])
                file.write('\n')

                location = '<div class="wise-iframe-wrapper"><iframe width="730" height="548" src="'+ data.iloc[i]['location'] +'" allowfullscreen></iframe></div>'
                file.write('%s\n'                        % location)
            file.close()






if __name__ == '__main__':
  

    # reading the CSV file
    csvFile = pandas.read_csv('test.csv')
    save_in_md_format(csvFile)