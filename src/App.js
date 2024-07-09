import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className='mainCont'>
      <h1>Speiseplan GUI</h1>

      <div className='tableDiv'>
        <table className='table table-hover'>
          <thead>
            <th scope="col">Betriebssystem</th>
            <th scope="col">Version</th>
            <th scope="col">Stand</th>
            <th scope="col">File</th>
            <th scope="col">Größe</th>
          </thead>
          <tbody>
            <tr>
            <td>Windows 10/11</td>
            <td>1.0</td>
            <td>08.07.2024</td>
            <td><a href="https://github.com/NotScottt/NotScottt.github.io/archive/refs/tags/Speiseplan_v.1.0.zip" download>Speiseplan_v.1.0.zip</a></td>
            <td>mehr als 130MB</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
