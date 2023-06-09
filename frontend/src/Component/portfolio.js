export const Portfolio = () => {
  return (
    <div id="portfolio" class="section lb">
      <div class="container">
        <div class="section-title text-left">
          <h3 class="ds-heading">Portfolio</h3>
        </div>

        <div class="gallery-menu row">
          <div class="col-md-12">
            <div class="button-group filter-button-group text-left">
              <button class="active" data-filter="*">
                All
              </button>
              <button data-filter=".gal_a">Web Development</button>
              <button data-filter=".gal_b">Python Modules</button>
              <button data-filter=".gal_c">Machine learning</button>
              <button data-filter=".gal_c">Publication</button>
            </div>
          </div>
        </div>

        <div class="row">
          <div class="col-md-4 col-sm-6 gal_a">
            <div class="post-box gallery-single fix">
              <div class="post-thumb">
                <img
                  src="uploads/blog-01.jpg"
                  class="img-fluid"
                  alt="post-img"
                />
              </div>
              <div class="post-info">
                <a href="https://familysooq.com">
                  <h4>Familysooq</h4>
                </a>
                <p>
                  Worked for a modern and easy-to-use platform, a marketplace
                  that is created for Ethiopians that provides buyers and
                  sellers with an avenue to exchange and trade goods and
                  services.
                </p>
              </div>
            </div>
          </div>
          <div class="col-md-4 col-sm-6 gal_b">
            <div class="post-box gallery-single fix">
              <div class="post-thumb">
                <img
                  src="uploads/blog-01.jpg"
                  class="img-fluid"
                  alt="post-img"
                />
              </div>
              <div class="post-info">
                <a href="https://github.com/Andalus-ICPC">
                  <h4>Andalus Online Judge</h4>
                </a>
                <p>
                  Andalus Online Judge is an online automated judge for
                  competitive programming contests and problem-solving. It is
                  hosted by Adama Science and Technology University to train
                  students for the ICPC (International Collegiate Programming
                  Contest).
                </p>
              </div>
            </div>
          </div>
          <div class="col-md-4 col-sm-6 gal_c">
            <div class="post-box gallery-single fix">
              <div class="post-thumb">
                <img
                  src="uploads/blog-01.jpg"
                  class="img-fluid"
                  alt="post-img"
                />
              </div>
              <div class="post-info">
                <a href="https://pypi.org/project/telebirrweb">
                  <h4>telebirrWeb PyPI</h4>
                </a>
                <p>Telebir Web.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
