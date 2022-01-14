import pandas as pd


def start():
    csv_file = "user_data1.csv"
    users_df = pd.read_csv(csv_file)
    print(users_df)
    user_df = users_df.loc[users_df['user_name'] != 'tazan']
    print(user_df)
    user_df.to_csv('user_data1.csv', index=False)

    print()


if __name__ == '__main__':
    start()
