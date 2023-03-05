import { DownloadIcon } from '@chakra-ui/icons';
import { Box, Button, FormControl, FormLabel, HStack, Input, InputGroup, InputLeftElement, Modal, ModalBody, ModalCloseButton, ModalContent, ModalFooter, ModalHeader, ModalOverlay, Select, Stack, Tag, TagCloseButton, TagLabel, Textarea } from '@chakra-ui/react'
import React from 'react'

interface LoginModalProps {
	isOpen: boolean,
	onClose: () => void,
	cover: string,
	setCover: (cover: string) => void,
}

const CreateProjectModal: React.FC<LoginModalProps> = ({ isOpen, onClose, cover, setCover }) => {

	const inputRef = React.createRef<HTMLInputElement>();

	const choicedStack = ["Node.js", "Product Manager", "Design/UI"]

	const choicedTags = choicedStack.map(item =>
		<Tag size={'lg'} key={item} colorScheme={"blue"} variant="outline">
			<TagLabel>{item}</TagLabel>
			<TagCloseButton />
		</Tag>
	)

	return (
		<Modal isOpen={isOpen} onClose={onClose} isCentered>
			<ModalOverlay />
			<ModalContent maxW={'812px'}>
				<ModalHeader fontSize={"2xl"} >Створити проєкт</ModalHeader>
				<ModalCloseButton />
				<ModalBody>
					<Stack spacing={4}>
						<Box
							display={'flex'}
							alignItems="center"
							gap={'6'}
						>
							<FormControl flexShrink={'50%'}>
								<FormLabel>Назва проєкту </FormLabel>
								<InputGroup>
									<Input type="text" />
								</InputGroup>
							</FormControl>
							<FormControl flexShrink={'50%'}>
								<FormLabel> Обкладинка </FormLabel>
								<InputGroup>
									<InputLeftElement
										pointerEvents="none"
										children={<DownloadIcon />}
									/>
									<input type='file' accept={'acceptedFileTypes'} onChange={(e) => setCover(e.target)} ref={inputRef} style={{ display: 'none' }} />
									<Input
										onClick={() => inputRef?.current?.click()}
										placeholder="Оберіть файл"
										value={cover && cover.files[0].name}
										readOnly
									/>
								</InputGroup>
							</FormControl>
						</Box>
						<Box>
							<FormControl>
								<FormLabel>Опис проєкту</FormLabel>
								<Textarea placeholder='Опишіть детально свій проєкт, що потрібно буде робити кожному з команди та які потрібні для нього спеціалісти' _placeholder={{ opacity: 0.7 }} />
							</FormControl>
						</Box>
						<Box
							display={'flex'}
							gap={'6'}
						>
							<FormControl flexShrink={'50%'}>
								<FormLabel>Додати необхідних спеціалістів </FormLabel>
								<Select placeholder='Обрати'>
									<option value='option1'>Option 1</option>
									<option value='option2'>Option 2</option>
									<option value='option3'>Option 3</option>
								</Select>
							</FormControl>
							<FormControl flexShrink={'50%'}>
								<FormLabel>Обрані спеціалісти </FormLabel>
								<Box display="flex" flexWrap={'wrap'} gap="2">
									{choicedTags}
								</Box>
							</FormControl>
						</Box>
					</Stack>
				</ModalBody>


				<ModalFooter >
					<HStack spacing="2">
						<Button size={'md'} colorScheme="gray" onClick={onClose} >Скасувати</Button>
						<Button size={'md'} colorScheme="blue" >Створити</Button>
					</HStack>
				</ModalFooter>
			</ModalContent>
		</Modal>
	)
}

export default CreateProjectModal;
