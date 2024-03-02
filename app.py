@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-template')
def get_template():
    return jsonify({
        'status': 'success',
        'word' : random.choice(templates)
    })

templates = [
    {
        'inputs' : 5,
        'category': 'Sports',
        'word': 'Chess',
    },
    {
        'inputs' : 6,
        'category' : 'European Country Name',
        'word' : 'France'
    },
    {
        'inputs' : 7,
        'category':'Sports',
        'word' : 'Tennis'
    },
        {
        'inputs' : 8,
        'category':'Sports',
        'word' : 'Skiing'
    },
        {
        'inputs' : 10,
        'category':'Sports',
        'word' : 'Cycling'
    },
        {
        'inputs' : 11,
        'category':'Sports',
        'word' : 'Cricket'
    },
        {
        'inputs' : 12,
        'category':'Sports',
        'word' : 'Squash'
    },
        {
        'inputs' : 13,
        'category':'Sports',
        'word' : 'Badminton'
    },
    {
        'inputs' : 14,
        'category':'Sports',
        'word' : 'Swimming'
    },
        {
        'inputs' : 15,
        'category':'Sports',
        'word' : 'Football'
    },

]