import streamlit as st
from datetime import date

st.title("🎂 Smart Age Calculator")

st.write("Enter your birth date to know interesting facts about your age!")

today = date.today()

birth_date = st.date_input(
    "Select your birth date",
    min_value=date(1900,1,1),
    max_value=today
)

if st.button("Calculate Age"):

    # Age calculation
    age_years = today.year - birth_date.year
    age_months = today.month - birth_date.month
    age_days = today.day - birth_date.day

    if age_days < 0:
        age_months -= 1
        age_days += 30

    if age_months < 0:
        age_years -= 1
        age_months += 12

    st.success(f"🎉 Your Age: {age_years} years, {age_months} months, {age_days} days")

    # Total days lived
    total_days = (today - birth_date).days
    st.write(f"📅 You have lived approximately **{total_days} days**.")

    # Age in hours
    hours = total_days * 24
    st.write(f"⏱ That's about **{hours} hours**!")

    # Next birthday
    next_birthday = date(today.year, birth_date.month, birth_date.day)

    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)

    days_left = (next_birthday - today).days
    st.write(f"🎂 Days until your next birthday: **{days_left} days**")

    # Birthday message
    if today.month == birth_date.month and today.day == birth_date.day:
        st.balloons()
        st.success("🎉 Happy Birthday! 🎂🎈")