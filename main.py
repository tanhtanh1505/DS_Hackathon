import pandas as pd
import map

train_work = pd.read_csv('./content/work_train.csv')
test_work = pd.read_csv('./content/work_test.csv')
train_info = pd.read_csv('./content/info_train.csv')
test_info = pd.read_csv('./content/info_test.csv')
y_train = pd.read_csv('./content/label_train.csv')

train = pd.merge(train_work, y_train, on='id_bh', how="inner")
train.drop_duplicates(subset='id_bh', keep='last', inplace=True)

train = pd.merge(train, train_info, on='id_bh', how='inner')

Y_train = train['label'].values

drop_field = ['id', 'id_bh', 'address_y', 'address_x', 
              'id_office', 
              'id_management',
              ]

test = pd.merge(test_work, test_info, on='id_bh', how="inner")
test.drop_duplicates(subset='id_bh', keep='last', inplace=True)

id_bh = test['id_bh']

test.drop(columns=drop_field, inplace=True)
train.drop(columns=drop_field, inplace=True)


train['bithYear'] = 2022 - train['bithYear']
test['bithYear'] = 2022 - test['bithYear']


train['job/role'] = train['job/role'].str.lower()
test['job/role'] = test['job/role'].str.lower()

train['job/role'] = train['job/role'].str.replace(r'[^ \w+]', "")
test['job/role'] = test['job/role'].str.replace(' +', ' ')
train['job/role'] = train['job/role'].str.replace(r'[^ \w+]', "")
test['job/role'] = test['job/role'].str.replace(' +', ' ')

train['job/role'].fillna('ngừng việc', inplace=True)
test['job/role'].fillna('ngừng việc', inplace=True)

map.age(train)
map.age(test)
map.job(train)
map.job(test)
map.job_time(train)
map.job_time(test)

train.drop(columns=['label'], inplace=True)

frames = [train,test]
merged = pd.concat(frames)

merged.to_csv('data.csv',index=False)

from sklearn.preprocessing import OneHotEncoder, MaxAbsScaler, StandardScaler, MinMaxScaler, OrdinalEncoder
from sklearn.decomposition import PCA, TruncatedSVD 
from sklearn.compose import ColumnTransformer

job_list = [['LDQL', 'NV', 'CMBC', 'CMBT', 'LDNLT', 'TVH', 'LDGD', 'LLVT', 'NA']]

job_encoder = OneHotEncoder(categories=job_list, handle_unknown='ignore')
encoder = OneHotEncoder()
lv_encoder = OrdinalEncoder()
transformers = [('c', encoder, [
                                'company_type',
                                'gender', 
                                'employee_lv', 
                                'bithYear']
                 ),
                ('j',job_encoder, ['job/role']),
]
column_trans = ColumnTransformer(transformers)
column_trans.fit(merged)
X_train = column_trans.transform(train)
X_test = column_trans.transform(test)

from sklearn.model_selection import train_test_split

trainX, testX, trainY, testY = train_test_split(X_train,Y_train,test_size=0.3,random_state=0)

from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import LinearRegression, SGDClassifier, LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB,CategoricalNB
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from lightgbm import LGBMClassifier

# model = XGBClassifier(
#     objective='multi:softmax',
#     max_depth=10, learning_rate=0.1, n_estimators=1000,
#     num_class=7,
#     tree_method = "gpu_hist",
# )
model = SVC()
model.fit(X_train,Y_train)
res = model.predict(X_test)
res_out = pd.DataFrame({'id_bh':id_bh,'label':res})
res_out.to_csv('result.csv',index=False)
print(cross_val_score(model, X_train, Y_train,verbose=3, cv=5))


