from calendar import Calendar

from flask import Flask, render_template, request, redirect, url_for, session,flash

from Forms import CreateUserForm, CreateReview, updateReview, CreateUserBMI, CreateUserPayment, AddProductForm, \
    LoginUserForm, UpdateUserBMI, CreateUserReview, CreateStatusForm, AddUserImage, UpdateUserForm

from flask_uploads import configure_uploads, UploadSet, IMAGES, UploadNotAllowed

from werkzeug.exceptions import RequestEntityTooLarge

import shelve, User, Review,  Bmi, Payment, Product, CalendarProgram, Status

from staff import Staff


app = Flask(__name__)
app.config['SECRET_KEY'] = "Thisismysecretkey"
app.config['SECRET_KEY'] = "Thisismysecretkey"
app.config['UPLOADED_IMAGES_DEST'] = 'static/images'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

image = UploadSet('images', IMAGES)
configure_uploads(app, image)

#Cecila and Li En
@app.route('/')
def to_home():
    review_dict = {}
    db = shelve.open('GoFit.db', 'r')
    review_dict = db['Review']
    db.close()

    review_list = []
    for key in review_dict:
        userReview = review_dict.get(key)
        review_list.append(userReview)

    users_dict = {}
    db = shelve.open('GoFit.db', 'r')
    users_dict = db['Users']
    db.close()

    # Get all the user object into a list
    users_list = []
    for key in users_dict:
        users_list.append(users_dict[key])

    # To separate the different memberships
    beginner_list = []
    standard_list = []
    intermediate_list = []

    for user in users_list:
        if user.get_membership() == 'B':  # Value that has been assigned
            beginner_list.append(user)
            continue
        elif user.get_membership() == 'S':
            standard_list.append(user)
            continue
        elif user.get_membership() == 'I':
            intermediate_list.append(user)
            continue
        else:
            print('The membership user entered is invalid.')  # For error prevention

    return render_template('home.html',review_list=review_list, count_beginner=len(beginner_list), count_standard=len(standard_list), count_intermediate=len(intermediate_list),count_users=len(users_list))

@app.route('/membership/signup/<plan>')
def membership_signup(plan):
    user_dict = {}
    db = shelve.open('GoFit.db')
    user_dict = db['Users']


    user = user_dict.get(session['user_id'])
    user.set_membership(plan)
    db['Users'] = user_dict
    db.close()

    return redirect(url_for('profile'))

@app.route('/membership')
def to_membership():
    users_dict = {}
    db = shelve.open('GoFit.db', 'r')
    users_dict = db['Users']
    db.close()

    # Get all the user object into a list
    users_list = []
    for key in users_dict:
        users_list.append(users_dict[key])

    # To separate the different memberships
    beginner_list = []
    standard_list = []
    intermediate_list = []

    for user in users_list:
        if user.get_membership() == 'B':  # Value that has been assigned
            beginner_list.append(user)
            continue
        elif user.get_membership() == 'S':
            standard_list.append(user)
            continue
        elif user.get_membership() == 'I':
            intermediate_list.append(user)
            continue
        else:
            print('The membership user entered is invalid.')  # For error prevention

    return render_template('membership.html', users_list=users_list, beginner_list=beginner_list, standard_list=standard_list, intermediate_list=intermediate_list,
                           count_beginner=len(beginner_list), count_standard=len(standard_list), count_intermediate=len(intermediate_list),count_users=len(users_list))

# Cecila (Admin)
@app.route('/admin')
def to_admin():

    users_dict = {}
    db = shelve.open('GoFit.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('admin/admin.html', count=len(users_list), users_list=users_list)


# Li En (Dashboard)
@app.route('/dashboard')
def to_dashboard():
    return render_template('admin/dashboard.html')

# Review CRUD (Li En)

@app.route('/createReview', methods=['GET', 'POST'])
def create_user_rev():
    create_user_form = CreateReview(request.form)
    if request.method == 'POST' and create_user_form.validate():
        staff_dict = {}
        db = shelve.open('GoFit.db', 'c')

        try:
            staff_dict = db['Review']
        except:
            print("Error in retrieving Users from Gofit.db.")
        staff = Review.userReview( first_name=create_user_form.first_name.data,
                                   last_name=create_user_form.last_name.data,
                                   review=create_user_form.review.data)

        staff_dict[staff.get_user_id()] = staff
        db['Review'] = staff_dict

        db.close()

        return redirect(url_for('review'))
    return render_template('createReview.html', form=create_user_form)

@app.route('/review')
def review():
    staff_dict = {}
    db = shelve.open('GoFit.db', 'w')
    staff_dict=db['Review']
    db.close()

    staff_list = []
    for key in staff_dict:
        staff = staff_dict.get(key)
        staff_list.append(staff)

    return render_template('review.html', count=len(staff_list), staff_list=staff_list)


# @app.route('/updateReview/<id>', methods=['GET','POST'])
# def update_review(id):
#     update_review_form = updateReview(request.form)
#     if request.method == 'POST' and update_review_form.validate():
#         reviews_dict = {}
#         db = shelve.open('GoFit.db', 'w')
#         reviews_dict = db['Review']
#
#         user = reviews_dict.get(id)
#         user.set_review(update_review_form.review.data)
#
#
#         db['Review'] = reviews_dict
#         db.close()
#
#         return redirect(url_for('review'))
#     else:
#         #loading the data review entered
#         reviews_dict = {}
#         db = shelve.open('GoFit.db', 'r')
#         reviews_dict = db['Review']
#         db.close()
#
#         user = reviews_dict.get(id)
#         update_review_form.review.data = user.get_review()
#
#
#         return render_template('updateReview.html', form=update_review_form,id=user.get_user_id())


# @app.route('/deleteReview/<id>', methods=['POST'])
# def delete_review(id):
#     staff_dict = {}
#     db = shelve.open('GoFit.db', 'w')
#     staff_dict = db['Review']
#
#     staff_dict.pop(id)
#
#     db['Review'] = staff_dict
#     db.close()
#
#     return redirect(url_for('review'))

# BMI CRUD (Li En)

@app.route('/createUserBMI', methods=['GET', 'POST'])
def create_user_bmi():
    create_bmi_form = CreateUserBMI(request.form)
    if request.method == 'POST' and create_bmi_form.validate():
        bmi_dict = {}
        db = shelve.open('GoFit.db', 'c')


        try:
            bmi_dict = db['bmi']

        except:
            print("Error in retrieving Users from GoFit.db.")
        user = Bmi.userBMI(
                           height=create_bmi_form.height.data,
                           weight=create_bmi_form.weight.data)

        bmi_dict[user.get_user_id()] = user
        db['bmi'] = bmi_dict

        db.close()

        return redirect(url_for('bmi'))
    return render_template('createUserBMI.html', form=create_bmi_form)

@app.route('/bmi')
def bmi():
    bmi_dict = {}
    db = shelve.open('GoFit.db', 'r')
    bmi_dict = db['bmi']
    db.close()

    bmi_list = []
    for key in bmi_dict:
        user = bmi_dict.get(key)
        bmi_list.append(user)

    return render_template('bmi.html', count=len(bmi_list), bmi_list=bmi_list)


@app.route('/updateBMI/<id>/', methods=['GET', 'POST'])
def update_bmi(id):
    update_bmi_form = UpdateUserBMI(request.form)
    if request.method == 'POST' and update_bmi_form.validate():
        bmi_dict = {}
        db = shelve.open('GoFit.db', 'w')
        bmi_dict = db['bmi']

        user = bmi_dict.get(id)
        user.set_height(update_bmi_form.height.data)
        user.set_weight(update_bmi_form.weight.data)


        db['bmi'] = bmi_dict
        db.close()


        return redirect(url_for('bmi'))
    else:
        bmi_dict = {}
        db = shelve.open('GoFit.db', 'r')
        bmi_dict = db['bmi']
        db.close()

        user = bmi_dict.get(id)

        update_bmi_form.height.data = user.get_height()
        update_bmi_form.weight.data = user.get_weight()


        # for readonly , theres why thr is user_id=user.get_user_id
        return render_template('updateBMI.html', form=update_bmi_form,user_id=user.get_user_id())

        # update_bmi_form

@app.route('/deleteBMI/<id>', methods=['POST'])
def delete_BMI(id):
    bmi_dict = {}
    db = shelve.open('GoFit.db', 'w')
    bmi_dict = db['bmi']

    bmi_dict.pop(id)

    db['bmi'] = bmi_dict
    db.close()

    return redirect(url_for('bmi'))


# Cecila (Settings) , li En (Reviews)
@app.route('/profile', methods=['GET', 'POST'])
def to_profile():
    review_dict = {}
    db = shelve.open('GoFit.db', 'r')
    review_dict = db['Review']

    review_list= []
    update_user_form = UpdateUserForm(request.form)

    users_dict = db['Users']
    keys = users_dict.keys()
    user_obj = users_dict.get(session['user_id'])

    for key in keys:
        user = users_dict[key]
        if (user.get_username() == str(session['username'])):
            update_user_form.first_name.data = user.get_first_name()
            update_user_form.last_name.data = user.get_last_name()
            update_user_form.email.data = user.get_email()
            update_user_form.contact_number.data = user.get_contact_number()

    db.close()
    for key in review_dict:
        userReview = review_dict.get(key)
        print("Review : " + str(userReview.get_user_id()))
        print(session['user_id'])
        # append the review list to the current user
        if userReview.get_user_id() == (session['user_id']):
            print("Added")
            review_list.append(userReview)
    if request.method == 'POST' and update_user_form.validate():
        print(request.form)
        db = shelve.open('GoFit.db', 'c')

        users_dict = db['Users']

        keys = users_dict.keys()
        username = request.form.get("login_username")
        for key in keys:
            user = users_dict[key]
            print("user.get_username() : " + str(user.get_username()))# test codes to print users
            print("str(session['username']) : " + str(session['username']))
            if(user.get_username() == str(session['username'])):# form check
                if(user.get_password() == request.form.get("current_password")):
                    print("update")
                    user.set_first_name(request.form.get("first_name"))
                    user.set_last_name(request.form.get("last_name"))
                    user.set_password(request.form.get("password"))
                    user.set_email(request.form.get("email"))
                    user.set_contact_number(request.form.get("contact_number"))

                    session['first_name'] = user.get_first_name()
                    session['last_name'] = user.get_last_name()
                    users_dict[key] = user
                    db['Users'] = users_dict

                    update_user_form.first_name.data = user.get_first_name()
                    update_user_form.last_name.data = user.get_last_name()
                    update_user_form.email.data = user.get_email()
                    update_user_form.contact_number.data = user.get_contact_number()
                    db.close()
                else:

                    update_user_form.current_password.errors.append("Wrong current password. Unable to update.")

        update_user_form.current_password.data = ""
        update_user_form.password.data = ""
        update_user_form.password_confirm.data = ""
        return render_template('login/profile.html',review_list=review_list, update_user_form=update_user_form,user_obj=user_obj)
    else:
        return render_template('login/profile.html',review_list=review_list, update_user_form=update_user_form,user_obj=user_obj)

#Li En (for users to create review)
@app.route('/createUserReview',methods=['GET','POST'])
def createUserReview():
    create_user_form = CreateUserReview(request.form)
    if request.method == 'POST' and create_user_form.validate():
        review_dict = {}
        db = shelve.open('GoFit.db', 'c')

        try:
            review_dict = db['Review']
        except:
            print("Error in retrieving Users from Gofit.db.")
        review = Review.userReview( session['user_id'],session['first_name'], session['last_name'],review=create_user_form.review.data)

        review_dict[review.get_user_id()] = review
        db['Review'] = review_dict

        db.close()
        return redirect(url_for('to_profile'))
    return render_template("userReview.html",form=create_user_form)

#Li En (for users to update review)
@app.route('/updateUserReview/<id>', methods=['GET','POST'])
def updateUserReview(id):
    update_review_form = updateUserReview(request.form)
    if request.method == 'POST' and update_review_form.validate():
        reviews_dict = {}
        db = shelve.open('GoFit.db', 'w')
        reviews_dict = db['Review']

        user = reviews_dict.get(id)
        user.set_review(update_review_form.review.data)


        db['Review'] = reviews_dict
        db.close()

        return redirect(url_for('to_profile'))
    else:
        #loading the data review entered
        reviews_dict = {}
        db = shelve.open('GoFit.db', 'r')
        reviews_dict = db['Review']
        db.close()

        user = reviews_dict.get(id)


    return render_template('updateUserReview.html', form=update_review_form,id=user.get_user_id)


# Cecila (Login and Signup)
@app.route('/signup', methods=('GET', 'POST'))
def to_register():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('GoFit.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from GoFit.db.")

        user = User.User(create_user_form.username.data, create_user_form.first_name.data, create_user_form.last_name.data,
                         create_user_form.password.data, create_user_form.email.data, create_user_form.contact_number.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict
        db.close()

        session['username'] = user.get_username()
        session['type'] = "user"

        return redirect(url_for('to_login'))
    return render_template('login/signup.html', form=create_user_form)

#Li En (sign out) and Cecila
@app.route('/signout')
def signOut():
    session.clear()
    return redirect(url_for('to_home'))

@app.route('/login', methods=['GET', 'POST'])
def to_login():
    login_user_form = LoginUserForm(request.form)
    if request.method == 'POST' and login_user_form.validate():
        db = shelve.open('GoFit.db', 'r')

        users_dict = db['Users']

        keys = users_dict.keys()
        username = request.form.get("login_username")
        password = request.form.get("login_password")
        for key in keys:
            user = users_dict[key]
            if user.get_username() == username and user.get_password() == password:
                session['username'] = user.get_username()
                if (type(user) == Staff):
                    session['type'] = "staff"
                    session['user_id'] = (user.get_user_id())
                    session['first_name'] = user.get_first_name()
                    session['last_name'] = user.get_last_name()
                    return render_template('admin/dashboard.html', form=login_user_form, type=session['type'], user=session['username'])
                elif (type(user) == User.User):
                    session['type'] = "user"
                    session['user_id'] = (user.get_user_id())
                    session['first_name'] = user.get_first_name()
                    session['last_name'] = user.get_last_name()
                    # return render_template('login/profile.html', form=login_user_form, type=session['type'], user=session['username'])
                    return redirect(url_for('to_profile'))
                else:
                    return "False"
        return "Login Failed"
    else:
        return render_template('login/login.html', form=login_user_form)



# Li En (Workout Lvls)
@app.route('/program/workout_level.html')
def to_workout_level():
    return render_template('program/workout_level.html')

# Li En ( Workout choices)
@app.route('/program/workout_level/<choice>')
def workout_level_select(choice):
    if 'type' not in session:
        return redirect(url_for('to_login'))

    users_dict = {}
    db = shelve.open('GoFit.db', 'c')
    try:
        users_dict = db['Users']
    except:
        print('something went wrong, and its cause of u :3')

    user_obj = users_dict.get(session['user_id'])
    # Users_dict = { user_id : user_obj }
    user_obj.set_membership(choice)
    print(user_obj.get_full_name(), user_obj.get_membership())
    db['Users'] = users_dict
    db.close()
    return redirect(url_for('to_profile'))

# Cecila (Program Calendar)
@app.route('/program/calendar.html', methods=['GET', 'POST'])
def to_calendar():
    cal_dict = {}

    if request.method == 'GET':
        # db = shelve.open('GoFit.db', 'w')
        # db['Calendars'] = {}
        # db.close()

        db = shelve.open('GoFit.db', 'r')
        cal_dict = db['Calendars']
        db.close()

        cal_dict2 =  {}
        for key in cal_dict:
            cal_dict2[key] =  {'title': cal_dict[key].get_name(), 'date': cal_dict[key].get_date()}
        print(cal_dict2)
        return render_template('program/calendar.html',events=cal_dict2)
    else:
        if('id' in request.form):
            if(request.form['title'] != ""):
                print("UPDATE")

                cal_dict = {}
                db = shelve.open('GoFit.db', 'w')
                cal_dict = db['Calendars']

                cal = cal_dict.get(request.form['id'])
                cal.set_name(request.form['title'])


                db['Calendars'] = cal_dict
                db.close()

            else: #delte
                cal_dict = {}
                db = shelve.open('GoFit.db', 'w')
                cal_dict = db['Calendars']

                cal_dict.pop(request.form['id'])

                db['Calendars'] = cal_dict
                db.close()

        else:
            title = request.form['title']
            date = request.form['date']
            cal = CalendarProgram.add_calendar(date+title,date,title)

            db = shelve.open('GoFit.db', 'w')

            try:
                cal_dict = db['Calendars']
            except:
                print("Error in retrieving Calendars from storage.db")
                db['Calendars'] =  cal_dict


            cal_dict[cal.get_key()] = cal

            db['Calendars'] = cal_dict
            db.close()

        return redirect(url_for('to_calendar'))


# # Cecila (Program)
# @app.route('/program/program.html')
# def to_program():
#     return render_template('program/program.html')

# Li En (BMI Checker)
@app.route('/bmichecker.html', methods=['POST', 'GET'])
def to_bmichecker():

    bmi=''
    if request.method == 'POST' and 'weight' in request.form and'height' in request.form:

        weight=float(request.form.get("weight"))
        height=float(request.form.get("height"))
        bmi=round(weight/((height/100)**2),2)
        db = shelve.open('GoFit.db','w')
        bmi_dict = db['bmi']

        bmi_obj = bmi_dict.get(session['user_id'])
        print(bmi_dict)
        print(bmi_obj)

        if bmi_obj is None:
            bmi_obj = Bmi.userBMI(session['user_id'], height,weight)

        else:
            bmi_obj.set_weight(request.form.get('weight'))
            bmi_obj.set_height(request.form.get('height'))
        bmi_dict[session['user_id']]= bmi_obj
        db['bmi' ] = bmi_dict
    return render_template('program/bmichecker.html',bmi=bmi)


# Li En (Rating)
@app.route('/testimonia')
def to_ratings():
            review_dict = {}
            db = shelve.open('GoFit.db', 'r')
            review_dict = db['Review']
            db.close()

            review_list= []
            for key in review_dict:
                userReview = review_dict.get(key)
                review_list.append(userReview)

            return render_template('shop/testimonia.html',review_list=review_list)

#profile image selection
@app.route('/login/addProfileimg.html',methods=['GET','POST'])
def addProfileimg():
    form = AddUserImage(request.form)
    if request.method == 'POST' and form.validate():
        db = shelve.open('GoFit.db', 'w')
        users_dict = {}

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from storage.db")


        try:
            img_filename = image.save(request.files['user_img'])

            #update
            user_obj = users_dict.get(session['user_id'])
            user_obj.set_user_img(img_filename)

            db['Users'] =users_dict


            db.close()
        except UploadNotAllowed:
            flash(f'File Type Unsupported, Please try again!', category='danger')
            return redirect(url_for('login/addProfileimg'))

        except RequestEntityTooLarge:
            flash(f'File Size Exceeded, Please Try again!', category='danger')
            return redirect(url_for('login/addProfileimg'))

        flash(f'Profile Image Successfully added!', category='success')

        return redirect(url_for('to_profile'))

    return render_template('login/addProfileimg.html', form=form)

# Suen Hong (Shop Cart)
@app.route('/shop/newShop.html')
def to_newshop():
    product_dict = {}
    db = shelve.open('GoFit.db', 'r')
    product_dict = db['Products']
    db.close()

    product_list= []
    for key in product_dict:
        userProduct = product_dict.get(key)
        product_list.append(userProduct)

    return render_template('/shop/newShop.html', product_list=product_list)

@app.route('/shop/newShop/add', methods=['GET', 'POST'])
def addProduct():
    form = AddProductForm(request.form)
    if request.method == 'POST' and form.validate():
        db = shelve.open('GoFit.db', 'w')
        products_dict = {}


        try:
            products_dict = db['Products']
        except:
            print("Error in retrieving Users from storage.db")


        try:
            img_filename = image.save(request.files['product_img'])


            product = Product.add_product(img_filename, form.product_name.data, form.product_price.data)
            products_dict[product.get_product_name()] = product


            db['Products'] = products_dict


            db.close()
        except UploadNotAllowed:
            flash(f'File Type Unsupported, Please try again!', category='danger')
            return redirect(url_for('addProduct'))
        except RequestEntityTooLarge:
            flash(f'File Size Exceeded, Please Try again!', category='danger')
            return redirect(url_for('addProduct'))

        flash(f'Product Successfully added!', category='success')

        return redirect(url_for('to_newshop'))

    return render_template('addProduct.html', form=form)

@app.route('/retrieveProduct')
def retrieve_product():
    product_dict = {}
    db = shelve.open('GoFit.db', 'r')
    product_dict = db['Products']
    db.close()

    product_list = []
    for key in product_dict:
        product = product_dict.get(key)
        product_list.append(product)

    return render_template('retrieveProduct.html', product_list=product_list)

@app.route('/updateProduct/<id>/', methods=['GET', 'POST'])
def update_product(id):
    form = AddProductForm(request.form)
    if request.method == 'POST' and form.validate():
        products_dict = {}
        db = shelve.open('GoFit.db', 'w')
        products_dict = db['Products']

        product = products_dict.get(id)
        product.set_product_name(form.product_name.data)
        product.set_product_price(form.product_price.data)


        db['Products'] = products_dict
        db.close()

        return redirect(url_for('retrieve_product'))
    else:
        products_dict = {}
        db = shelve.open('GoFit.db', 'r')
        products_dict = db['Products']
        db.close()

        product = products_dict.get(id)
        form.product_name.data = product.get_product_name()
        form.product_price.data = product.get_product_price()

    return render_template('updateProduct.html', form=form)

@app.route('/deleteProduct/<id>', methods=['POST'])
def delete_product(id):
    product_dict = {}
    db = shelve.open('GoFit.db', 'w')
    product_dict = db['Products']

    product_dict.pop(id)

    db['Products'] = product_dict
    db.close()

    return redirect(url_for('retrieve_product'))

# Suen Hong (Shop Cart)
@app.route('/shop/cart.html')
def to_cart():
    return render_template('/shop/cart.html')

# Li En (Trending)
@app.route('/shop/trending.html')
def to_trending():
    product_dict = {}
    db = shelve.open('GoFit.db', 'r')
    product_dict = db['Products']
    db.close()

    product_list = []
    for key in product_dict:
        product = product_dict.get(key)
        product_list.append(product)

    return render_template('/shop/trending.html', product_list=product_list)


# Suen Hong ( Shop Payment)
@app.route('/shop/payment.html', methods=['GET', 'POST'])
def to_payment():
    create_user_payment = CreateUserPayment(request.form)
    if request.method == 'POST' and create_user_payment.validate():
        payment_dict = {}
        db = shelve.open('GoFit.db', 'c')


        try:
            payment_dict = db['Payment']
        except:
            print("Error in retrieving Users from storage.db.")


        payment = Payment.user_payment(card_number=create_user_payment.card_number.data, card_name=create_user_payment.card_name.data,
                                       card_exp=create_user_payment.card_exp.data, card_cvc=create_user_payment.card_cvc.data)
        payment_dict[payment.get_card_number()] = payment
        db['Payment'] = payment_dict


        db.close()
        session['user_created'] = payment.get_card_name()

        return redirect(url_for('to_home'))
    return render_template('/shop/payment.html', form=create_user_payment)

@app.route('/retrievePayment')
def retrieve_payment():
    payment_dict = {}
    db = shelve.open('GoFit.db', 'r')
    payment_dict = db['Payment']
    db.close()

    payment_list = []
    for key in payment_dict:
        payment = payment_dict.get(key)
        payment_list.append(payment)

    return render_template('retrivePayment.html', count=len(payment_list), payment_list=payment_list)

@app.route('/updatePayment/<int:id>/', methods=['GET', 'POST'])
def update_payment(id):
    update_user_payment = CreateUserPayment(request.form)
    if request.method == 'POST' and update_user_payment.validate():
        payment_dict = {}
        db = shelve.open('GoFit.db', 'c')
        payment_dict = db['Payment']

        payment = payment_dict.get(id)
        payment.set_card_number(update_user_payment.card_number.data)
        payment.set_card_name(update_user_payment.card_name.data)
        payment.set_card_exp(update_user_payment.card_exp.data)
        payment.set_card_cvc(update_user_payment.card_cvc.data)

        db['Payment'] = payment_dict
        db.close()

        session['user_updated'] = payment.get_card_name()

        return redirect(url_for('retrieve_payment'))
    else:
        payment_dict = {}
        db = shelve.open('GoFit.db', 'r')
        payment_dict = db['Payment']
        db.close()

        payment = payment_dict.get(id)
        update_user_payment.card_number.data = payment.get_card_number()
        update_user_payment.card_name.data = payment.get_card_name()
        update_user_payment.card_exp.data = payment.get_card_exp()
        update_user_payment.card_cvc.data = payment.get_card_cvc()

    return render_template('updatePayment.html', form=update_user_payment)

@app.route('/deletePayment/<int:id>', methods=['POST'])
def delete_payment(id):
    payment_dict = {}
    db = shelve.open('GoFit.db', 'w')
    payment_dict = db['Payment']

    payment = payment_dict.pop(id)

    db['Payment'] = payment_dict
    db.close()

    session['user_deleted'] = payment.get_card_name()

    return redirect(url_for('retrieve_payment'))


# Matthew (Status)
@app.route('/createStatus', methods=['GET', 'POST'])
def create_status():
    create_status_form = CreateStatusForm(request.form)
    if request.method == 'POST' and create_status_form.validate():
        status_dict = {}
        db = shelve.open('GoFit.db', 'c')
        try:
            status_dict = db['Status']
        except:
            print("Error in retrieving Users from storage.db.")

        status = Status.Status(create_status_form.status.data)
        status_dict[status.get_status_id()] = status
        db['Status'] = status_dict
        db.close()

        session['status_created'] = status.get_status_id()

        return redirect(url_for('after_create_status'))
    return render_template('createStatus.html', form=create_status_form)


@app.route('/createStatus(after)')
def after_create_status():
    return render_template('createStatus(after).html')


@app.route('/retrieveStatus')
def retrieve_status():
    status_dict = {}
    db = shelve.open('GoFit.db', 'r')
    status_dict = db['Status']
    db.close()

    status_list = []
    for key in status_dict:
        status = status_dict.get(key)
        status_list.append(status)

    return render_template('retrieveStatus.html', count=len(status_list), status_list=status_list)


@app.route('/updateStatus/<int:id>/', methods=['GET', 'POST'])
def update_status(id):
    update_status_form = CreateStatusForm(request.form)
    if request.method == 'POST' and update_status_form.validate():
        status_dict = {}
        db = shelve.open('GoFit.db', 'w')
        status_dict = db['Status']

        status = status_dict.get(id)
        status.set_status(update_status_form.status.data)

        db['Status'] = status_dict
        db.close()

        return redirect(url_for('to_profile'))
    else:
        status_dict = {}
        db = shelve.open('GoFit.db', 'r')
        status_dict = db['Status']
        db.close()

        status = status_dict.get(id)
        update_status_form.status.data = status.get_status()

        return render_template('updateStatus.html', form=update_status_form)


@app.route('/deleteStatus/<int:id>', methods=['POST'])
def delete_status(id):
    status_dict = {}
    db = shelve.open('GoFit.db', 'w')
    status_dict = db['Status']

    status = status_dict.pop(id)

    db['Status'] = status_dict
    db.close()

    return redirect(url_for('to_profile'))


# Li En (Error Page)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404

def initData():
    db = shelve.open('GoFit.db', writeback=True)
    # users_dict = db['Users']
    # # user = Staff("AdminLogin", "AdFirstName", "AdLastName", "password")
    # # users_dict[user.get_user_id()] = user
    # db.close()

if __name__ == '__main__':
    initData()
    app.run(debug=True)
