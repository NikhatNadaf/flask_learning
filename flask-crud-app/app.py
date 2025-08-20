from flask import Flask, request, render_template, redirect, url_for
from supabase import create_client, Client
# Add Supabase URL and API Key 
SUPABASE_URL = "https://aapshvcoklnyzkqdgycx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFhcHNodmNva2xueXprcWRneWN4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTUxNTU2MzksImV4cCI6MjA3MDczMTYzOX0.9K0nygbFRiWED3z167iflsRwzVYkXnUxiXpEjHEdVwk"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)


# ------------------- Home / Read -------------------
@app.route('/')
def index():
    response = supabase.table("my_users").select("*").execute()
    print("response: ",response)
    users = response.data
    return render_template('index.html', users=users)

# ------------------- Create -------------------
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # Example: Insert into Supabase table "my_users"
        supabase.table("my_users").insert({
            "name": name,
            "email": email
        }).execute()
        return redirect(url_for('index'))
    return render_template('create.html')

# ------------------- Update -------------------
@app.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update(user_id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        supabase.table("my_users").update({
            "name": name,
            "email": email
        }).eq("id", user_id).execute()
        return redirect(url_for('index'))

    user = supabase.table("my_users").select("*").eq("id", user_id).single().execute().data
    return render_template('update.html', user=user)

# ------------------- Delete -------------------
@app.route('/delete/<int:user_id>', methods=['POST'])
def delete(user_id):
    supabase.table("my_users").delete().eq("id", user_id).execute()
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
