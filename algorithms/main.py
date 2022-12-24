from tkinter import *
from Learning_KNN import knn_algo
from Learning_SVM import svm_algo
from Naive_Bayes import naive_algo
from Logistic_Regression import logistic_algo
from Decision_Tree import decision_algo

window = Tk()

window.title("Prediction App")
window.resizable(False, False)

## Global variables ##
ageVal = StringVar()
deptVal = StringVar()
locVal = StringVar()
eduVal = StringVar()
recuitVal = StringVar()
levelVal = StringVar()
rateVal = StringVar()
onsiteVal = StringVar()
awardsVal = StringVar()
certifVal = StringVar()
salaryVal = StringVar()
## variable for radio buttons ##
var = StringVar()

depts = ["HR", "Sales", "Technology", "Purchasing"]  # options for menu
locs = ["City", "Suburb"]
edus = ["PG", "UG"]
recuits = ["Recruitme", "Referral", "On-campus", "Walk-in"]


window.geometry('{}x{}'.format(810, 810))
Label(window, width=810,text="The Model is ready for prediction",
      font=('Helvetica', 18, 'bold'),pady=10,padx=20,fg='White',bg='#19284F').pack()


bottomFrame = Frame(window)
bottomFrame.pack()
bottomFrame.config(width=100, height=800, relief=RIDGE, pady=20)



chosenAlgo = ""


def declare_entries():
    global ageVal, deptVal, locVal, eduVal, recuitVal, levelVal, rateVal, onsiteVal, awardsVal, certifVal, salaryVal

    Label(bottomFrame, text="Enter your age {20 to 60}", pady=10, fg='#0A2647').grid(row=0, column=0)
    age = Entry(bottomFrame, width=25, borderwidth=2, textvariable=ageVal)
    age.grid(row=1, column=0)

    Label(bottomFrame, text="\t\tSelect your department\t\t", padx=10, pady=10, fg='#0A2647').grid(row=0, column=1)
    deptVal.set("HR")  # default value
    o1 = OptionMenu(bottomFrame, deptVal, *depts)
    o1.config(width=20)
    o1.grid(row=1, column=1)

    Label(bottomFrame, text="Select your Location", pady=10, fg='#0A2647').grid(row=2, column=0)
    locVal.set("City")  # default value
    o2 = OptionMenu(bottomFrame, locVal, *locs)
    o2.config(width=20)
    o2.grid(row=3, column=0)

    Label(bottomFrame, text="\t\tSelect your education\t\t", pady=10, fg='#0A2647').grid(row=2, column=1)
    eduVal.set("PG")  # default value
    o3=OptionMenu(bottomFrame, eduVal, *edus)
    o3.config(width=20)
    o3.grid(row=3, column=1)

    Label(bottomFrame, text="Select your recruitment_type", pady=10, fg='#0A2647').grid(row=4, column=0)
    recuitVal.set("Referral")  # default value
    o4=OptionMenu(bottomFrame, recuitVal, *recuits)
    o4.config(width=20)
    o4.grid(row=5, column=0)

    Label(bottomFrame, text="Enter your job level {1 to 5}", pady=10, fg='#0A2647').grid(row=4, column=1)
    level = Entry(bottomFrame, width=25, borderwidth=2, textvariable=levelVal, fg='#0A2647')
    level.grid(row=5, column=1)

    Label(bottomFrame, text="Enter your rating {1 to 5}", pady=10, fg='#0A2647').grid(row=6, column=0)
    rate = Entry(bottomFrame, width=25, borderwidth=2, textvariable=rateVal, fg='#0A2647')
    rate.grid(row=7, column=0)

    Label(bottomFrame, text="Are onsite {0 for NO or 1 for YES}", pady=10, fg='#0A2647').grid(row=6, column=1)
    onsite = Entry(bottomFrame, width=25, borderwidth=2, textvariable=onsiteVal, fg='#0A2647')
    onsite.grid(row=7, column=1)
    Label(bottomFrame, text="Enter your awards {0 to 9}", pady=10, fg='#0A2647').grid(row=8, column=0)
    awards = Entry(bottomFrame, width=25, borderwidth=2, textvariable=awardsVal, fg='#0A2647')
    awards.grid(row=9, column=0)
    Label(bottomFrame, text="Has certifications? {0 for NO or 1 for YES}", pady=10, fg='#0A2647').grid(row=8, column=1)
    certifications = Entry(bottomFrame, width=25, borderwidth=2, textvariable=certifVal, fg='#0A2647')
    certifications.grid(row=9, column=1)
    Label(bottomFrame, text="Enter your salary ", pady=10, fg='#0A2647').grid(row=10, column=0)
    salary = Entry(bottomFrame, width=25, borderwidth=2, textvariable=salaryVal, fg='#0A2647')
    salary.grid(row=11, column=0)


def message_print(textInput):
    mini_window = Toplevel(window)
    mini_window.minsize(300, 200)
    Label(mini_window, text=textInput, font="90", fg="Navyblue", pady=50).pack(anchor=CENTER)
    Button(mini_window,bg='Navyblue',fg='White',width=30,padx=5,pady=5,text="OK",
           command=lambda: mini_window.destroy()).pack(anchor=CENTER)

def choose_algo(algo):
    global chosenAlgo
    chosenAlgo = algo

def algorithms():
    Label(window, width=810,text="Select Preferred Algorithm", pady=7
          , font=('Helvetica', 18, 'bold'),fg='White',bg='#19284F').pack(anchor=CENTER)

    Label(window,text="",pady=2).pack(anchor=CENTER)

    global var
    var.set("naivebayes")
    choose_algo("naivebayes")

    # Radiobutton(window, text="K-Mean", variable=var, padx=340,
    #             value="kmean", command=lambda: choose_algo("kmean")).pack(anchor=W)

    Radiobutton(window, text="KNN", variable=var, padx=340,
                value="knn", command=lambda: choose_algo("knn")).pack(anchor=W)

    Radiobutton(window, text="SVM", variable=var, padx=340,
                value="svm", command=lambda: choose_algo("svm")).pack(anchor=W)

    Radiobutton(window, text="Logistic", variable=var, padx=340,
                value="logistic", command=lambda: choose_algo("logistic")).pack(anchor=W)

    Radiobutton(window, text="Naive Bayes", variable=var, padx=340,
                value="naivebayes", command=lambda: choose_algo("naivebayes")).pack(anchor=W)

    Radiobutton(window, text="Decision Tree", variable=var, padx=340,
                value="decision", command=lambda: choose_algo("decision")).pack(anchor=W)

    Label(window,text="",pady=4).pack(anchor=CENTER)

    Button(window, width=50, pady=8, text="Confirm",bg='Orange', command=execute_algo).pack(anchor=CENTER)


result = ""

def execute_algo():
    global result
    test_case = [ageVal.get(), depts.index(deptVal.get()), locs.index(locVal.get()), edus.index(eduVal.get()),
                 recuits.index(recuitVal.get()), levelVal.get(), rateVal.get(), onsiteVal.get(),
                 awardsVal.get(), certifVal.get(), salaryVal.get()]


## Validate entries ##

    if ageVal.get().isalpha() or ageVal.get() == "":
        message_print("AGE should be in range 20,60")
    elif levelVal.get().isalpha() or levelVal.get() == "":
        message_print("Your LEVEL must be in range 1,5")
    elif rateVal.get().isalpha() or rateVal.get() == "":
        message_print("Your RATE must be in range 1,5")
    elif onsiteVal.get().isalpha() or onsiteVal.get() == "":
        message_print("ONSITE value must be 0 or 1")
    elif awardsVal.get().isalpha() or awardsVal.get() == "":
        message_print("Your AWARDS must be in range 1,9")
    elif certifVal.get().isalpha() or certifVal.get() == "":
        message_print("Your CERTIFICATIONS must be in 0 or 1")
    elif salaryVal.get().isalpha() or salaryVal.get() == "":
        message_print("Salary must be 10K or more")
    else:
        if int(ageVal.get()) < 20 or int(ageVal.get()) > 60:
            message_print("AGE should be in range 20,60")
        elif int(levelVal.get()) < 1 or int(levelVal.get()) > 5:
            message_print("Your LEVEL must be in range 1,5")
        elif int(rateVal.get()) < 1 or int(rateVal.get()) > 5:
            message_print("Your RATE must be in range 1,5")
        elif int(onsiteVal.get()) < 0 or int(onsiteVal.get()) > 1:
            message_print("ONSITE value must be 0 or 1")
        elif int(awardsVal.get()) < 1 or int(awardsVal.get()) > 9:
            message_print("Your AWARDS must be in range 1,9")
        elif int(certifVal.get()) < 0 or int(certifVal.get()) > 1:
            message_print("Your CERTIFICATIONS must be in 0 or 1")
        elif int(salaryVal.get()) < 10000:
            message_print("Your SALARY must be 10k or more")
        else:
            if chosenAlgo == "knn":
                result = knn_algo(test_case)
            # if chosenAlgo == "kmean":
            #     result = k_mean_algo(test_case)
            elif chosenAlgo == "svm":
                result = svm_algo(test_case)
            elif chosenAlgo == "decision":
                result = decision_algo(test_case)
            elif chosenAlgo == "logistic":
                result = logistic_algo(test_case)
            elif chosenAlgo == "none":
                message_print("Please select an algorithm first")
            else:
                result = naive_algo(test_case)
            sub_win = Toplevel(window)
            sub_win.minsize(300, 300)
            Label(sub_win, text="Prediction of " + chosenAlgo, font="90", fg="Navyblue", pady=50).pack(
                anchor=CENTER)
            if result[0] == 0:
                Label(sub_win, text=str("0 => Unsatisfied"), font="90", fg="Navyblue", pady=10).pack(anchor=CENTER)
            else:
                Label(sub_win, text=str("1 => Satisfied"), font="90", fg="Navyblue", pady=10).pack(anchor=CENTER)
            # Label(sub_win, text="Accuracy of " + chosenAlgo, font="90", fg="Navyblue", pady=10).pack(anchor=CENTER)
            # Label(sub_win, text=str(result[1]), font="90", fg="Navyblue", pady=10).pack(anchor=CENTER)

## The real start ##
declare_entries()
algorithms()



window.mainloop()
