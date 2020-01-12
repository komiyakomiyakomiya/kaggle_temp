# %%
import os
import pickle


# %%
class Data(object):
    def __init__(self):
        pwd = os.getcwd()
        if 'working' not in pwd:
            pwd = f'{pwd}/working'
            os.chdir(pwd)
            print(f'current_dir -> {pwd}')
        print(f'current_dir -> {pwd}')

    def _load(self):
        with open(f'../input/titanicdatasetpickles/train.pickle', 'rb') as f:
            train = pickle.load(f)

        with open(f'../input/titanicdatasetpickles/test.pickle', 'rb') as f:
            test = pickle.load(f)

        with open(f'../input/titanicdatasetpickles/gender_submission.pickle', 'rb') as f:
            gender_submission = pickle.load(f)

        return train, test, gender_submission

    def processing(self):
        train, test, gender_submission = self._load()

        Embarked_dict = {
            'S': 0,
            'C': 1,
            'Q': 2
        }
        train['Embarked'] = train['Embarked'].map(Embarked_dict)
        test['Embarked'] = test['Embarked'].map(Embarked_dict)

        Sex_dict = {
            'male': 0,
            'female': 1
        }
        train['Sex'] = train['Sex'].map(Sex_dict)
        test['Sex'] = test['Sex'].map(Sex_dict)

        train.drop(['PassengerId', 'Name', 'Cabin',
                    'Ticket'], axis=1, inplace=True)
        test.drop(['PassengerId', 'Name', 'Cabin',
                   'Ticket'], axis=1, inplace=True)

        # X_trainはtrainのSurvived列以外
        X_train = train.drop(['Survived'], axis=1)
        y_train = train['Survived']  # Y_trainはtrainのSurvived列

        return X_train, y_train, test, gender_submission


if __name__ == '__main__':
    data = Data()
    X_train, y_train, test, gender_submission = data.processing()
    display(X_train)


# %%
