<center>Fachpräsentation Customer Clustering</center>  
<center>DLBDSIDS01_D - Kurs: Einführung in Data Science</center>  
<center>Aufgabenstellung 2 -  Clustering und Kunden-Segmentierung in der Marktforschung</center>  

**Voraussetzungen:**
- Python 3.x
- ggf. make  

**Einrichtung mit make:**  
 - make prepare in der Konsole ausführen  
   
**Einrichtung ohne make:**  
 - virtuelle Python Umgebung erzeugen:  
    python3 -m venv venv  
 - virtuelle Umgebung aktivieren:  
    Windows -> venv\Scripts\activate  
    Linux/Mac -> source venv/bin/activate  
 - Abhängigkeiten aus der requirements.txt installieren:  
    pip install -r requirements.txt  
  
**Aufbau des Projektes:**  
- data 
    - imaginary_customers.csv -> Rohdaten
- images
    - methods.png -> Elbow / Silhouette Score Method Ergebnis
    - visualization.png -> Visualisierung des Ergebnisses
- notebooks
    - exploration.ipynb -> jupyter notebook mit dem Code
