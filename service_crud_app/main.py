from flask import Flask, render_template, request, redirect, url_for
from supabase import create_client, Client
# Add  Supabase URL and API Key 
SUPABASE_URL = "https://aapshvcoklnyzkqdgycx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFhcHNodmNva2xueXprcWRneWN4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTUxNTU2MzksImV4cCI6MjA3MDczMTYzOX0.9K0nygbFRiWED3z167iflsRwzVYkXnUxiXpEjHEdVwk"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)


# ------------------- Home / Read -------------------
@app.route('/')
def index():
    response = supabase.table("services").select("*").execute()
    print("response: ",response)
    services = response.data  
    return render_template('index.html', services=services)

# ------------------- Create -------------------
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']

        # Example: Insert into Supabase table "services"
        supabase.table("services").insert({
            "name": name,
            "description": description,
            "price": price
        }).execute()

        return redirect(url_for('index'))

    return render_template('create.html')


# ------------------- Update -------------------
@app.route('/update/<int:service_id>', methods=['GET', 'POST'])
def update(service_id):
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']

        supabase.table("services").update({
            "name": name,
            "description": description,
            "price": price
        }).eq("id", service_id).execute()

        return redirect(url_for('index'))

    service = supabase.table("services").select("*").eq("id", service_id).single().execute().data
    return render_template('update.html', service=service)

# ------------------- Delete -------------------
@app.route('/delete/<int:service_id>', methods=['POST'])
def delete(service_id):
    supabase.table("services").delete().eq("id", service_id).execute()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)