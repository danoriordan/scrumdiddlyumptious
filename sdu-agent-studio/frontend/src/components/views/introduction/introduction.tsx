import * as React from "react";
import { Button } from "antd";
import { ChevronLeftIcon } from "@heroicons/react/24/outline";
import { navigate } from "gatsby";

// Optional: Import a local image
import myImage from "../../../images/agents-cpd.webp";  // Adjust the path accordingly

const IntroductionView: React.FC = () => {

  return (
    <div>
      {/* Image display */}
      <div style={{ width: '100%', textAlign: 'center', marginBottom: '20px' }}>
        <img
          src={myImage} // Change to URL if using an online image
          alt="Descriptive Alt Text"
          style={{ width: '50%', height: 'auto' }} // Adjust sizing as needed
        />
      </div>
    </div> // Add a closing curly brace here
  );
};

export default IntroductionView;
