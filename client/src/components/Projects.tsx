import { Box, Button, Grid, GridItem, Heading, Stack } from '@chakra-ui/react'
import React from 'react'
import { IProjectItem } from '../models/IProjectItem'
import Layout from './Layout'
import ProjectItem from './ProjectItem'

interface ProjectsProps {
	title: string,
	items: IProjectItem[],
	withButton?: boolean,
	onCreate?: () => void,
}

const Projects: React.FC<ProjectsProps> = ({ title, items, withButton, onCreate }) => {

	const projectItems = items.map((item, idx) => <GridItem key={idx} > <ProjectItem {...item} /> </GridItem>)



	return (
		<Box>
			<Stack spacing={5}>
				<Box display={'flex'} alignItems="center" gap={2} justifyContent="space-between" mb>
					<Heading as='h2' size='lg'>{title}</Heading>
					{withButton ? <Button colorScheme={"blue"} size={'md'} onClick={onCreate}> Створити проект </Button> : null}
				</Box>

				<Grid gridTemplateColumns={'repeat(3, 1fr)'} gap="5">
					{projectItems}
				</Grid>
			</Stack>
		</Box>
	)
}

export default Projects
