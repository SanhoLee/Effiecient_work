#calculate linear interpolation with (x, f(x)) list data,
# and x input for solving
def linear_interpolation(
    x,
    f_list
):
    '''
    f(x)をf_listの変数群の範囲で内挿する

    Parameters
    ----------
    x : float
        独立変数
    f_list : np.array((0,2))
        独立変数、従属変数のリスト
    '''

    val1List = []
    val2List = []
    i = 0
    y = 0
    for f in f_list:
        if x < f[0] and i > 0:
            val1List = f_list[i-1]
            val2List = f_list[i]
            break
        i += 1

    y = val1List[1] + ((val2List[1]-val1List[1]) /
                       (val2List[0]-val1List[0])) * (x - val1List[0])

    return y

# input will be the Data from reading pandas, 
# and return list of each column data!
# from first row , read column data and get length of column for first row, 
# and make each column data to list data
def all_to_column(data_all):
    len_col = len(data_all[0:1, :][0])
    return [data_all[:, i] for i in range(len_col)]


# get ndarray data
def get_ndarray(list_x, list_y):
    return np.array([[list_x[i], list_y[i]] for i in range(len(list_x))])


# input : pair of list, return interpolated y value
def get_intpol_Y_list(x_input, list_pair):
    return list(map(lambda x: linear_interpolation(x, list_pair), x_input))


def get_avg(list1, list2):
    return (list1+list2)/2

#no need to consider number of list, can add any number of lists. 
# recommend to use this rather than upper one.
def get_avg2(*df_list_name):
    length = len(df_list_name)
    set_sum = 0
    for i in df_list_name:
        set_sum +=i   


# make csv file with dataframe-data
def df_to_file(df_name, filepath):
    dir_name = os.path.dirname(filepath)

    if(os.path.isdir(dir_name)):
        df_name.to_csv(filepath, index=False)
    else:
        os.mkdir(dir_name)
        df_name.to_csv(filepath, index=False)

# when working for training data process.
def df_to_file2(df_name, case_no, rad):
    cur_dir = os.getcwd()

    dir_name = os.path.join(cur_dir, 'tstrain_force_csv')
    if(os.path.isdir(dir_name)):
        os.chdir(dir_name)
        df_name.to_csv(
            f'initial_sample_strain_load_{case_no}_R{rad}.csv', index=False)
    else:
        os.mkdir(dir_name)
        os.chdir(dir_name)
        df_name.to_csv(
            f'initial_sample_strain_load_{case_no}_R{rad}.csv', index=False)

# get csv file with Ux - force pair data.
def get_Ux_and_force(solver_name,neu_file, radius_xNode, Load_yNode):
    os.system('{solver_name} {neu_file} -vecXID 2 -vecYID 53 -entityXID {radius_xNode} -entityYID {Load_yNode}'.format(
        solver_name=solver_name,
        neu_file=neu_file,
        radius_xNode=radius_xNode,
        Load_yNode=Load_yNode
    ))


# Return CSV file name , it is made for a file that is made by NeuPostXY something.
def get_csv_name(input, XRes, YRes, XNd, YNd):
    FILENAME = '{input}.pos.X_{XRes}_{XNd}_Y_{YRes}_{YNd}.csv'.format(
        input=input,
        XRes=XRes,
        YRes=YRes,
        XNd=XNd,
        YNd=YNd
        )
    return FILENAME
