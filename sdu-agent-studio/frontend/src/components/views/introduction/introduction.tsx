import * as React from "react";
import { Button } from "antd";
import { ChevronLeftIcon } from "@heroicons/react/24/outline";
import { navigate } from "gatsby";

// Optional: Import a local image
import myImage from "../../../images/agents-cpd.webp";  // Adjust the path accordingly
import myUsecase from "../../../images/usecase.png";  // Adjust the path accordingly

const IntroductionView: React.FC = () => {

  return (
    <React.Fragment>
      <React.Fragment>
        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '20px' }}>
          {/* Image display */}
          <div style={{ width: '50%', textAlign: 'left' }}>
            <img
              src={myImage} // Change to URL if using an online image
              alt="Descriptive Alt Text"
              style={{ width: '100%', height: 'auto' }} // Adjust sizing as needed
            />
          </div>
          {/* Image display */}
          <div style={{ width: '50%', textAlign: 'right' }}>
            <img
              src={myUsecase} // Change to URL if using an online image
              alt="Descriptive Alt Text"
              style={{ width: '100%', height: 'auto' }} // Adjust sizing as needed
            />
          </div>
        </div>
      </React.Fragment>
    </React.Fragment>

  );
};

export default IntroductionView;
