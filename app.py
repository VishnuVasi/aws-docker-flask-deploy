from flask import Flask
import boto3

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Hello! I am Vasanth M</h1>
    <p>Observability Platform Engineer @ PayPal</p>
    <p>This app is Dockerised and deployed on AWS EC2</p>
    '''

@app.route('/health')
def health():
    return {'status': 'running', 'message': 'App is healthy!'}


@app.route('/s3')
def read_s3():
    s3 = boto3.client('s3', region_name='ap-south-1')
    obj = s3.get_object(Bucket='vasanth-flask-bucket', Key='message.txt')
    message = obj['Body'].read().decode('utf-8')
    return f'''
    <div style="background:#080c14;color:#00e5ff;font-family:monospace;
    padding:2rem;min-height:100vh;">
    <h2>📦 Message from S3 Bucket</h2>
    <br>
    <p style="color:#e2e8f0;font-size:1.1rem">{message}</p>
    <br>
    <a href="/" style="color:#f59e0b">← Back to Portfolio</a>
    </div>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)