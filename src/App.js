import './App.css';

function App() {
  function displayInfos(whichElem) {
    // console.log(whichElem)

    if (whichElem === "infoButton1") {
      let infoModal1 = document.getElementById("infoModal_1")
      var button1Span = document.getElementById("closeButton1");

      infoModal1.style.display = "block";
      button1Span.onclick = function() {
        infoModal1.style.display = "none";
      }

    } else if (whichElem === "infoButton2") {
      let infoModal2 = document.getElementById("infoModal_2")
      var button2Span = document.getElementById("closeButton2");

      infoModal2.style.display = "block";
      button2Span.onclick = function() {
        infoModal2.style.display = "none";
      }
    }
    
  }

  function alertForDownload() {
    alert("Hello World")
  }

  const ItemNotAvailable = () => {
    return(
      <td>Aktuell nicht verfügbar.</td>
    )
  } 

  const showItems = [false, false, true]

  return (
    <div className='mainCont'>
      <div className='tableDiv'>
        <table className='table table-hover'>
          <thead>
            <th scope="col">Item</th>
            <th scope="col">Info</th>
            <th scope="col">Betriebssystem</th>
            <th scope="col">Version</th>
            <th scope="col">Stand</th>
            <th scope="col">File</th>
            <th scope="col">Größe</th>
          </thead>
          <tbody>
            <tr>
              <td>Speiseplan Anwendung</td>
              <td><i className="fa fa-info-circle" id='infoButton2' onClick={(e) => displayInfos(e.target.id)}></i></td>
              <td>Windows 10/11</td>
              <td>1.0</td>
              <td>08.07.2024</td>
              {showItems[0] ? (
                <td><a href="https://github.com/NotScottt/react_speiseplan/archive/refs/tags/" download>Speiseplan_v.1.0.zip</a></td>
              ) : (
                <ItemNotAvailable />
              )}
              <td>/</td>
            </tr>
            <tr>
              <td>Installationsdateien</td>
              <td><i className="fa fa-info-circle" id="infoButton1" onClick={(e) => displayInfos(e.target.id)}></i></td>
              <td>Windows 10/11</td>
              <td>1.0</td>
              <td>08.07.2024</td>
              {showItems[1] ? (
                <td><a href="https://github.com/NotScottt/react_speiseplan/archive/refs/tags/" onclick={alertForDownload}>internal.zip</a></td>
              ) : (
                <ItemNotAvailable />
              )}
              
              <td>~ 270MB</td>
            </tr>
            <tr>
              <td>Gebündelt</td>
              <td></td>
              <td>Windows 10/11</td>
              <td>1.0</td>
              <td>08.07.2024</td>
              {showItems[2] ? (
                <td><a href="https://github.com/NotScottt/react_speiseplan/archive/refs/tags/BundlePlan.zip" download>Gebündelt</a></td>
              ) : (
                <ItemNotAvailable />
              )}
              <td>~ 300MB</td>
            </tr>
          </tbody>
        </table>

        
        
        <h2 id='installationHeader'>Installation</h2>
        <div id='installationDiv'>Die Installationsanleitung befindet sich <a href='https://github.com/NotScottt/react_speiseplan/blob/main/README.md'>hier</a>.</div>
      </div>


      {/* Modale */}
        <div id="infoModal_1" className="modal">
        <div className="modal-content">
          <span className="close" id='closeButton1'>&times;</span>
          <p>Dies ist ein Ordner, der alle Datein beinhaltet, die für die Desktopanwendung benötigt werden.<br/> Er ist allerdings sehr groß und sollte daher
            nur ein mal installiert werden.
          </p>
        </div>
      </div>

      <div id="infoModal_2" className="modal">
        <div className="modal-content">
          <span className="close" id='closeButton2'>&times;</span>
          <p>Dies ist die tatsächliche Desktopanwendung. Diese sollte installiert werden, sobald es ein Update gab.</p>
        </div>
      </div>
    </div>
  );
}

export default App;
