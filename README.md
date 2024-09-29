<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Project_Title_0"></a>Self Organizing Map And Anamolies Detection Using Neural Networks On Wholesale Customers Dataset</h1>
<h2 class="code-line" data-line-start=2 data-line-end=3 ><a id="Overview_2"></a>Overview</h2>
<p class="has-line-data" data-line-start="4" data-line-end="5">This project implements a Self-Organizing Map (SOM) using neural networks on the Wholesale Customers dataset from the UCI Machine Learning Repository. The tool visualizes the results and identifies anomalies in the dataset.</p>
<h2 class="code-line" data-line-start=6 data-line-end=7 ><a id="Hardware_Requirements_6"></a>Hardware Requirements</h2>
<p class="has-line-data" data-line-start="8" data-line-end="9">To run this project effectively, ensure that your system meets the following hardware specifications:</p>
<ul>
<li class="has-line-data" data-line-start="10" data-line-end="11"><strong>Processor</strong>: Dual-core processor (Intel i3 or equivalent)</li>
<li class="has-line-data" data-line-start="11" data-line-end="12"><strong>RAM</strong>: Minimum 4GB</li>
<li class="has-line-data" data-line-start="12" data-line-end="13"><strong>Disk Space</strong>: At least 500MB for the dataset and environment</li>
<li class="has-line-data" data-line-start="13" data-line-end="15"><strong>Operating System</strong>: Windows, macOS, or any Linux distribution</li>
</ul>
<h2 class="code-line" data-line-start=15 data-line-end=16 ><a id="Software_Requirements_15"></a>Software Requirements</h2>
<p class="has-line-data" data-line-start="17" data-line-end="18">Ensure you have the following software installed:</p>
<ul>
<li class="has-line-data" data-line-start="19" data-line-end="21"><strong>Python Version</strong>: Python 3.8 or higher</li>
</ul>
<h3 class="code-line" data-line-start=21 data-line-end=22 ><a id="Required_Libraries_21"></a>Required Libraries</h3>
<p class="has-line-data" data-line-start="23" data-line-end="24">The following libraries are required for the project. Install them using the provided <code>requirements.txt</code> file:</p>
<ul>
<li class="has-line-data" data-line-start="25" data-line-end="26"><code>numpy</code></li>
<li class="has-line-data" data-line-start="26" data-line-end="27"><code>pandas</code></li>
<li class="has-line-data" data-line-start="27" data-line-end="28"><code>matplotlib</code></li>
<li class="has-line-data" data-line-start="28" data-line-end="29"><code>scikit-learn</code></li>
<li class="has-line-data" data-line-start="29" data-line-end="31"><code>minisom</code></li>
</ul>
<h2 class="code-line" data-line-start=31 data-line-end=32 ><a id="Installation_Steps_31"></a>Installation Steps</h2>
<p class="has-line-data" data-line-start="33" data-line-end="34">Follow these steps to set up the environment and execute the project:</p>
<ol>
<li class="has-line-data" data-line-start="36" data-line-end="42">
<p class="has-line-data" data-line-start="36" data-line-end="38"><strong>Install Required Libraries</strong><br>
Open a terminal and run the following command to install the necessary libraries:</p>
<pre><code class="has-line-data" data-line-start="39" data-line-end="41" class="language-bash">pip install -r requirements.txt
</code></pre>
</li>
<li class="has-line-data" data-line-start="42" data-line-end="48">
<p class="has-line-data" data-line-start="42" data-line-end="44"><strong>Run the Main Script</strong><br>
Navigate to the directory where the <code>main.py</code> file is located and execute the script:</p>
<pre><code class="has-line-data" data-line-start="45" data-line-end="47" class="language-bash">python src/main.py
</code></pre>
</li>
</ol>
<h2 class="code-line" data-line-start=48 data-line-end=49 ><a id="Output_Files_48"></a>Output Files</h2>
<p class="has-line-data" data-line-start="50" data-line-end="51">Upon successful execution of the program, you will find two visual output files generated in the <code>visuals</code> folder:</p>
<ul>
<li class="has-line-data" data-line-start="52" data-line-end="53"><strong><code>matrix.png</code></strong>: This file contains the visual representation of the Self-Organizing Map.</li>
<li class="has-line-data" data-line-start="53" data-line-end="54"><strong><code>anomalies.png</code></strong>: This file highlights the identified anomalies in the dataset.</li>
</ul>
