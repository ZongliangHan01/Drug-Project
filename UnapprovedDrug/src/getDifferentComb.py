import pandas as pd

his_df = pd.read_csv('historical_data/approved_close_price.csv')

for k in range(30, 41):
    period = k

    headers = [
    '60B', '59B', '58B', '57B', '56B', '55B', '54B', '53B', '52B', '51B', '50B', 
    '49B', '48B', '47B', '46B', '45B', '44B', '43B', '42B', '41B', '40B', '39B', 
    '38B', '37B', '36B', '35B', '34B', '33B', '32B', '31B', '30B', '29B', '28B', 
    '27B', '26B', '25B', '24B', '23B', '22B', '21B', '20B', '19B', '18B', '17B', 
    '16B', '15B', '14B', '13B', '12B', '11B', '10B', '9B', '8B', '7B', '6B', '5B', 
    '4B', '3B', '2B', '1B', 'PDUFA', '1A', '2A', '3A', '4A', '5A', '6A', '7A', 
    '8A', '9A', '10A', '11A', '12A', '13A', '14A', '15A', '16A', '17A', '18A', 
    '19A', '20A', '21A', '22A', '23A', '24A', '25A', '26A', '27A', '28A', '29A', 
    '30A', '31A', '32A', '33A', '34A', '35A', '36A', '37A', '38A', '39A', '40A', 
    '41A', '42A', '43A', '44A', '45A', '46A', '47A', '48A', '49A', '50A', '51A', 
    '52A', '53A', '54A', '55A', '56A', '57A', '58A', '59A', '60A']    
    new_headers = []
    for i in range(0, len(headers)):
        if i + period < len(headers):  # Ensure there are at least 7 days of data remaining        
            new_header = headers[i] + 'T' + headers[i + period]
            new_headers.append(new_header)
        else:
            new_headers.append(headers[i])

    # Create headers from "one" to "twenty"
    # headers = [str(i) for i in range(0, 61)]

    # Create an empty dataframe with those headers
    df = pd.DataFrame(columns=new_headers)

    j = 0
    for index, row in his_df.iterrows():
        j += 1
        row_diff = []
        # change the row to list
        row = row.tolist()
        print(len(row))
        # Iterate over the columns in chunks of 7 days
        for i in range(1, len(row)):
            
            # Calculate the difference between the current value and the value 7 days ago
            if i + period < len(row):  # Ensure there are at least 7 days of data remaining
                print(row[i + period], row[i])
                diff = (row[i + period] - row[i])/row[i]*100
                row_diff.append(diff)
                print(diff)
            else:
                row_diff.append(None)  #
        print(len(row_diff))
        print(len(df.columns))
        df.loc[row[0]+str(j)] = row_diff

    # Display the dataframe
    print(df)
    # Save the dataframe to a CSV file
    means = df.mean()
    for i in range(len(means)):
        print(means[i])
    df.loc['mean'] = means
    # df = df.rename_axis("Company")
    # df = df.set_index(df.columns[0])
    df.to_excel(f'historical_data/{period}_approved_diff_close_price.xlsx')
    print(j)