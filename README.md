# history-enabled-calc
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Calculator with History - README</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }
        h2 {
            color: #34495e;
            margin-top: 30px;
        }
        code {
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            color: #e74c3c;
        }
        pre {
            background: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        pre code {
            background: none;
            color: #ecf0f1;
        }
        ul {
            padding-left: 25px;
        }
        li {
            margin: 8px 0;
        }
        .note {
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 12px;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Simple Calculator with History</h1>
        <p>A command-line calculator that performs basic arithmetic operations and saves calculation history to a file.</p>

        <h2>Features</h2>
        <ul>
            <li><strong>Basic Operations</strong>: Addition (+), Subtraction (-), Multiplication (*), Division (/)</li>
            <li><strong>History Tracking</strong>: Automatically saves all calculations to <code>history.txt</code></li>
            <li><strong>View History</strong>: Display past calculations in reverse chronological order</li>
            <li><strong>Clear History</strong>: Remove all saved calculations</li>
        </ul>

        <h2>Usage</h2>
        <p>Run the program:</p>
        <pre><code>python calculator.py</code></pre>

        <h3>Commands</h3>
        <ul>
            <li><strong>Perform calculation</strong>: Enter equation in format <code>number operator number</code>
                <ul>
                    <li>Example: <code>5 + 3</code>, <code>10 / 2</code>, <code>7 * 8</code></li>
                </ul>
            </li>
            <li><code>history</code>: View all past calculations</li>
            <li><code>clear</code>: Delete calculation history</li>
            <li><code>exit</code>: Quit the calculator</li>
        </ul>

        <h2>Example Session</h2>
        <pre><code>Welcome to a Simple Calculator
Type the equation: 5 + 3
Result: 8

Type the equation: 10 * 2
Result: 20

Type the equation: history
10 * 2=20
5 + 3=8

Type the equation: exit
Goodbye</code></pre>

        <h2>Notes</h2>
        <div class="note">
            <ul style="margin: 0;">
                <li>Calculations must have spaces between numbers and operators</li>
                <li>History is stored in <code>history.txt</code> in the same directory</li>
                <li>Division by zero is prevented with an error message</li>
            </ul>
        </div>
    </div>
</body>
</html>


