import Search from './components/search';
import HospitalDisplay from './components/HospitalDisplay';
import Cards from './components/Cards';
import SearchClass from './components/SearchClass';
import Header from './components/Header';
import Carousel from './components/Carousel';
import Footer from './components/Footer';
import CustomChatbot from './components/CustomChatbot';
import PieChart from './components/PieChart';
import { BrowserRouter as Router, Switch, Route, Redirect } from 'react-router-dom';
import Speciality from './components/Speciality';
import Contact from './components/Contact';
import DoctorCards from './components/DoctorCards';
import DoctorFetch from './components/DoctorFetch';





function App() {
  return (
    <div>
      <Router>
        <Header/>
        <Switch> 
          <Route exact path='/' component={Carousel} />
          <Route exact path='/' component={Carousel} />
          <Route exact path='/home' component={Carousel} />
          <Route exact path='/doc' component={DoctorCards} />
         
          <Route exact path='/about' component={PieChart} />
          {/* <Route exact path='/speciality' component={Speciality} /> */}
          <Route exact path='/hospitals' component={HospitalDisplay} />
          <Route exact path='/doctors' component={DoctorFetch} /> 
          <Route exact path='/cards' component={Cards} />        
        </Switch>
      </Router>
      <CustomChatbot />
         {/* <Footer />  */}
    </div>
  );
}

export default App;
