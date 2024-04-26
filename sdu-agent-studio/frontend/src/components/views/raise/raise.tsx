import * as React from "react";
import { Button } from "antd";
import { ChevronLeftIcon } from "@heroicons/react/24/outline";
import { navigate } from "gatsby";

const RAISEView: React.FC = () => {
  const iframeUrl = "http://52.152.169.134:8082/"; // Hardcoded URL to display

  return (
    <div>
  

      {/* Iframe to display the hardcoded URL */}
      <div style={{ width: '100%', height: '80vh', overflow: 'hidden' }}>
        <iframe
          src={iframeUrl}
          //title="RAISE Demo"
          style={{ width: '100%', height: '100%' }}
          frameBorder="0"
        ></iframe>
      </div>
    </div>
  );
};

export default RAISEView;
