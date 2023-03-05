import { useDisclosure } from '@chakra-ui/react'
import React from 'react'
import Layout from '../components/Layout'
import CreateProjectModal from '../components/modals/CreateProjectModal'
import Projects from '../components/Projects'
import { ProjectItemMockup, ProjectItemsMockup } from "../mockup.js"

const Home = () => {

  const { isOpen: isOpenCreateProject, onOpen: onOpenCreateProject, onClose: onCloseCreateProject } = useDisclosure()
  const [cover, setCover] = React.useState('')


  return (
    <Layout>
      <Projects title="Ваши проекти" items={ProjectItemsMockup} onCreate={onOpenCreateProject} withButton />
      <Projects title="Проєкти в яких шукають JavaScript / Front-End " items={ProjectItemsMockup} />



      <CreateProjectModal isOpen={isOpenCreateProject} cover={cover} setCover={setCover} onClose={onCloseCreateProject} />
    </Layout>
  )
}

export default Home
