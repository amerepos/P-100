from services import Restructure

if __name__ == '__main__':
    file_path = input("Enter input file path: ")
    sheet_name = input("Enter input sheet name: ")
    out_path = input("Enter output file path: ")

    # If no user input then set default values
    file_path = file_path if file_path else 'data/Analytics Template for Exercise.xlsx'
    sheet_name = sheet_name if sheet_name else 'input_refresh_template'
    out_path = out_path if out_path else 'data/output.xlsx'

    print('File path is ', file_path)
    print('Sheet name is ', sheet_name)
    print('Out path is ', out_path)
    print('-----------------------------------------')

    print('Starting....')
    restructure = Restructure(file_path=file_path,sheet_name=sheet_name, out_path=out_path)
    restructure.restructure_analytics_data()
    print('Done!')
