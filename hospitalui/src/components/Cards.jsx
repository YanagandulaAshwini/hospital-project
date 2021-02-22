import React from 'react';


const Cards = () => {
    return (
        <div className="doctorcards">
            <div class="card mb-3" style={{"max-width": "540px"}}>
  <div class="row no-gutters">
    <div class="col-md-4">
      {/* <svg class="bd-placeholder-img" style={{"width": "100%", "height":"300px"}} xmlns="https://i.pinimg.com/474x/1e/d7/b6/1ed7b68d268434b3b130f01bbff866d4.jpg" aria-label="Placeholder: Image" preserveAspectRatio="xMidYMid slice" role="img"><title>Placeholder</title><rect width="100%" height="100%" fill="#868e96"/><text x="50%" y="50%" fill="#dee2e6" dy=".3em">Image</text></svg> */}
      <img src="https://i.pinimg.com/474x/1e/d7/b6/1ed7b68d268434b3b130f01bbff866d4.jpg" class="card-img-top" />

    </div>
    <div class="col-md-8">
      <div class="card-body" style={{ "min-height":"300px"}}>
        <h5 class="card-title">Card title</h5>
        <p class="card-text">It's a broader card with text below as a natural lead-in to extra content. This content is a little longer.</p>
        <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
      </div>
    </div>
  </div>
</div>
                        </div>
                       
    )
}

export default Cards;