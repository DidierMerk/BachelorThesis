import boto3
import os

# Insert credentials
credentials_dir = '/home/jovyan/.aws'
if not os.path.exists(credentials_dir):
    os.makedirs(credentials_dir)

with open(credentials_dir + '/credentials', 'w') as f:
    f.write('[default]\n')
    f.write('aws_access_key_id=40644ce6817945868b382fc57a787739\n')
    f.write('aws_secret_access_key=517212e2ad9e4d7a81e63145e14338c4\n')
    
download_list = ['train_QuarkGluon.sh', 'env.sh', '.pt', '.py', '.parquet', 'qg']
dir_list = ['data', 'datasets', 'models', 'networks']    
    
# Make data directory
data_dir = '/home/jovyan/data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
    
# Make all other directories for good formatting
for directory in dir_list:
    data_dir = '/home/jovyan/data/{}'.format(directory)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
for directory in ['data', 'datasets']:
    data_dir = '/home/jovyan/data/{}/QuarkGluon'.format(directory)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

data_dir = '/home/jovyan/data'

client = boto3.client('s3', endpoint_url='https://s3.cern.ch')
for key in client.list_objects(Bucket='dejan')['Contents']:
    for name in download_list:
        if name in key['Key']:
            if name == 'train_QuarkGluon.sh':
                print('Downloading ', key['Key'])
                client.download_file('dejan', key['Key'], data_dir + '/' + key['Key'])
            elif name == 'env.sh':
                print('Downloading ', key['Key'])
                client.download_file('dejan', key['Key'], data_dir + '/' + key['Key'])                
            elif name == '.parquet':
                print('Downloading ', key['Key'])
                client.download_file('dejan', key['Key'], data_dir + '/datasets/QuarkGluon/' +  key['Key'])
            elif name == '.pt':
                print('Downloading ', key['Key'])
                client.download_file('dejan', key['Key'], data_dir + '/models/' +  key['Key'])
            elif name == '.py':
                print('Downloading ', key['Key'])
                client.download_file('dejan', key['Key'], data_dir + '/networks/' +  key['Key'])
            elif name == 'qg':
                print('Downloading ', key['Key'])
                client.download_file('dejan', key['Key'], data_dir + '/data/QuarkGluon/' +  key['Key'])