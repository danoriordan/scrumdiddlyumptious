import * as React from "react";
import Layout from "../../components/layout";
import { graphql } from "gatsby";
import RAView from "../../components/views/raise/raise";

// markup
const IndexPage = ({ data }: any) => {
  return (
    <Layout meta={data.site.siteMetadata} title="Capgemini" link={"/raise"}>
      <main style={{ height: "300%" }} className=" h-full ">
        <RAView />
      </main>
    </Layout>
  );
};

export const query = graphql`
  query HomePageQuery {
    site {
      siteMetadata {
        description
        title
      }
    }
  }
`;

export default IndexPage;
