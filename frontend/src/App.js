import { About } from "./Component/about";
import { Achievements } from "./Component/achievements";
import { Experience } from "./Component/experience";
import { Education } from "./Component/education";
import { Portfolio } from "./Component/portfolio";
import { Testimonials } from "./Component/testimonial";
import { Blog } from "./Component/blog";
import { Contact } from "./Component/contact";
import { Home } from "./Component/home";
import { NavBar } from "./Component/navBar";
import { Footer } from "./Component/footer";
function App() {
  return (
    <>
      <NavBar />
      <Home />
      <About />
      <Achievements />
      <Experience />
      <Education />
      <Portfolio />
      <Testimonials />
      <Blog />
      <Contact />
      <Footer />
    </>
  );
}

export default App;
