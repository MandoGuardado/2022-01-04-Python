import pandas as pd


def start():
    csv_file = "user_data1.csv"
    users_df = pd.read_csv(csv_file)
    print(users_df)
    print("\n")
    user_df = users_df.loc[users_df['user_name'] != 'tarzan']
    print(user_df)
    print("\n")
    user_df.to_csv('user_data1.csv', index=False)
    print(pd.read_csv(csv_file))

    with open('user_data1.csv', 'a') as fd:
        fd.write(f'\ntesttest,test,test123,25')
    print("\n")
    print(pd.read_csv(csv_file))


if __name__ == '__main__':
    start()
