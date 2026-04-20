import pandas as pd
import joblib
import os

def predict_attrition(new_data):
    try:
        model = joblib.load('model/model_attrition.pkl')
        model_columns = joblib.load('model/model_columns.pkl')
        df_encoded = pd.get_dummies(pd.DataFrame([new_data]))
        for col in model_columns:
            if col not in df_encoded.columns: df_encoded[col] = 0
        df_encoded = df_encoded[model_columns]
        return model.predict(df_encoded)[0], model.predict_proba(df_encoded)[0][1]
    except Exception as e:
        return None, str(e)

def menu():
    while True:
        print("\n=== SISTEM PREDIKSI RESIGN KARYAWAN ===")
        print("1. Cek Data Karyawan (Contoh)")
        print("2. Masukkan Data Manual (Simulasi)")
        print("0. Keluar")
        pilih = input("Pilih menu: ")

        if pilih == '1':
            data = {'Age': 24, 'BusinessTravel': 'Travel_Frequently', 'DailyRate': 450, 'Department': 'Sales', 'DistanceFromHome': 20, 'Education': 2, 'EducationField': 'Marketing', 'EnvironmentSatisfaction': 1, 'Gender': 'Female', 'JobLevel': 1, 'JobRole': 'Sales Representative', 'JobSatisfaction': 1, 'MaritalStatus': 'Single', 'MonthlyIncome': 2300, 'OverTime': 'Yes', 'TotalWorkingYears': 1, 'YearsAtCompany': 1}
            res, prob = predict_attrition(data)
            print(f"\nHasil: {'RESIGN' if res == 1 else 'STAY'} (Risiko: {prob*100:.2f}%)")
        
        elif pilih == '2':
            print("\n--- Input Data Singkat ---")
            umur = int(input("Umur: "))
            gaji = int(input("Gaji Bulanan: "))
            lembur = input("Lembur (Yes/No): ")
            data = {'Age': umur, 'MonthlyIncome': gaji, 'OverTime': lembur, 'JobLevel': 1, 'JobSatisfaction': 1}
            res, prob = predict_attrition(data)
            print(f"\nHasil Prediksi: {'RESIGN' if res == 1 else 'STAY'}")
            print(f"Probabilitas: {prob*100:.2f}%")

        elif pilih == '0':
            print("Selesai!")
            break
        else:
            print("Pilihan salah!")

if __name__ == "__main__":
    menu()